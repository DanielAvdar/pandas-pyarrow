from typing import Dict, List, Optional, Tuple, Any
import inspect

from .mappers import create_mapper

import numpy as np
import pandas as pd
import pyarrow as pa

# Global dict to track nested type columns
_NESTED_TYPE_COLUMNS = {}


class PandasArrowConverter:
    """PandasArrowConverter manages the conversion of Pandas DataFrame data types to Arrow data types.
    :param custom_mapper: dictionary with key as the source data type and value as the target data type.
    Will override default mapping
    :param default_target_type: Optional string specifying the default data type to use if no mapping is found for a
    specific data type. Default is "string[pyarrow]".
    :param detect_nested: Whether to detect and convert nested data types (lists, dictionaries) in object columns.
    Default is True.

    """

    def __init__(
        self,
        custom_mapper: Optional[Dict[str, str]] = None,
        default_target_type: Optional[str] = "string[pyarrow]",
        detect_nested: bool = True,
    ):
        self.additional_mapper_dicts = custom_mapper or {}
        self.defaults_dtype = default_target_type
        self.detect_nested = detect_nested
        self._mapper = create_mapper() | self.additional_mapper_dicts
        self.nested_type_registry = {}

    def __call__(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply a transformation to the dtypes of a Pandas DataFrame based on a mapping.

        The function adjusts the data types of the columns in the provided DataFrame.
        It uses the current dtypes of the DataFrame columns, processes them through
        a mapping function to get the corresponding target dtypes, and applies the
        mapping to create a new DataFrame with updated dtypes.

        If detect_nested is True, it will also attempt to detect columns containing
        lists or dictionaries and convert them to the appropriate PyArrow types.

        :param df: A Pandas DataFrame whose column dtypes will be transformed.
        :type df: pd.DataFrame
        :return: A new Pandas DataFrame with transformed column dtypes.
        :rtype: pd.DataFrame
        """
        # Clear the nested type registry
        self.nested_type_registry = {}
        
        dtype_names: List[str] = df.dtypes.astype(str).tolist()
        target_dtype_names = self._map_dtype_names(dtype_names)
        
        # Get column to dtype mapping
        col_to_dtype = dict(zip(df.columns, target_dtype_names))
        
        # Convert the DataFrame
        adf = df.astype({col: dtype for col, dtype in col_to_dtype.items()})
        
        # If detect_nested is enabled, handle nested types
        if self.detect_nested:
            adf = self._handle_nested_types(df, adf)
        
        # Store the nested types registry in the DataFrame as metadata
        adf._nested_types_registry = self.nested_type_registry
        
        return adf
        
    def _handle_nested_types(self, orig_df: pd.DataFrame, adf: pd.DataFrame) -> pd.DataFrame:
        """
        Handle nested data types by using PyArrow directly
        
        :param orig_df: Original DataFrame
        :param adf: DataFrame being processed
        :return: DataFrame with nested types properly handled
        """
        # Find object columns to check for nested types
        object_cols = [col for col in orig_df.columns if str(orig_df[col].dtype) == 'object']
        
        for col in object_cols:
            # Skip empty columns
            if orig_df[col].isna().all():
                continue
                
            # Get first non-null value to check its type
            sample = orig_df[col].dropna().iloc[0] if not orig_df[col].isna().all() else None
            
            if sample is not None:
                if isinstance(sample, list):
                    # Convert to PyArrow and back to capture the list structure
                    table = pa.Table.from_pandas(orig_df[[col]])
                    adf[col] = table.to_pandas()[col]
                    # Track as a list type column
                    self.nested_type_registry[col] = "list[pyarrow]"
                    
                elif isinstance(sample, dict):
                    # Convert to PyArrow and back to capture the dict structure
                    table = pa.Table.from_pandas(orig_df[[col]])
                    adf[col] = table.to_pandas()[col]
                    # Track as a struct type column
                    self.nested_type_registry[col] = "struct[pyarrow]"
        
        return adf
        
    def get_nested_dtypes(self, df: pd.DataFrame) -> Dict[str, str]:
        """
        Get the nested dtypes for a DataFrame that was processed by this converter
        
        :param df: DataFrame to get nested types for
        :return: Dictionary mapping column names to nested type names
        """
        return getattr(df, "_nested_types_registry", {})

    def _target_dtype_name(self, dtype_name: str) -> str:
        type_mapper = self._mapper
        defaults_dtype = self.defaults_dtype or dtype_name
        if "[pyarrow]" in dtype_name:
            return dtype_name
        return type_mapper.get(dtype_name, defaults_dtype)

    def _map_dtype_names(self, dtype_names: List[str]) -> List[str]:
        return [self._target_dtype_name(dtype_name) for dtype_name in dtype_names]
