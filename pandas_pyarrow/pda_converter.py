from typing import Dict, List, Optional

from .mappers import create_mapper

import pandas as pd


class PandasArrowConverter:
    """PandasArrowConverter manages the conversion of Pandas DataFrame data types to Arrow data types.
    :param custom_mapper: dictionary with key as the source data type and value as the target data type.
    Will override default mapping
    :param default_target_type: Optional string specifying the default data type to use if no mapping is found for a
    specific data type. Default is "string[pyarrow]".

    """

    def __init__(
        self,
        custom_mapper: Optional[Dict[str, str]] = None,
        default_target_type: Optional[str] = "string[pyarrow]",
    ):
        self.additional_mapper_dicts = custom_mapper or {}
        self.defaults_dtype = default_target_type
        self._mapper = create_mapper() | self.additional_mapper_dicts

    def __call__(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply a transformation to the dtypes of a Pandas DataFrame based on a mapping.

        The function adjusts the data types of the columns in the provided DataFrame.
        It uses the current dtypes of the DataFrame columns, processes them through
        a mapping function to get the corresponding target dtypes, and applies the
        mapping to create a new DataFrame with updated dtypes.

        :param df: A Pandas DataFrame whose column dtypes will be transformed.
        :type df: pd.DataFrame
        :return: A new Pandas DataFrame with transformed column dtypes.
        :rtype: pd.DataFrame
        """
        dtype_names: List[str] = df.dtypes.astype(str).tolist()
        target_dtype_names = self._map_dtype_names(dtype_names)
        adf = df.astype(dict(zip(df.columns, target_dtype_names)))
        return adf

    def _target_dtype_name(self, dtype_name: str) -> str:
        type_mapper = self._mapper
        defaults_dtype = self.defaults_dtype or dtype_name
        if "[pyarrow]" in dtype_name:
            return dtype_name
        return type_mapper.get(dtype_name, defaults_dtype)

    def _map_dtype_names(self, dtype_names: List[str]) -> List[str]:
        return [self._target_dtype_name(dtype_name) for dtype_name in dtype_names]
