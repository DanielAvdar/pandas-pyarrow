from typing import Dict, List, Optional

from .mappers import reverse_create_mapper

import numpy as np
import pandas as pd
import pyarrow as pa


class ReversePandasArrowConverter:
    """
    ReversePandasArrowConverter manages the conversion of pyarrow-backed Pandas DataFrame dtypes
    back to their Numpy/Pandas equivalents.

    :param custom_mapper: Dictionary with key as the string-representation of the
        Arrow-backed dtype, and value as the desired target dtype (e.g. "object", "int64", etc.).
        This overrides default mapping returned by reverse_create_mapper().
    :param default_target_type: Optional string specifying the default dtype to use
        if no mapping is found for a specific dtype. Default is "object".

    """

    def __init__(
        self,
        custom_mapper: Optional[Dict[str, str]] = None,
        default_target_type: Optional[str] = "object",
    ):
        self._mapper = reverse_create_mapper() | (custom_mapper or {})
        self._default_target_type = default_target_type

    def __call__(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Maps the data types of a given pandas DataFrame to the target data types
        specified by the object's internal mapping logic. This method processes
        the DataFrame by replacing its column data types according to the mapped
        target types and returns a new DataFrame with these updated data types.
        Any `NaN` values are handled accordingly during the process.

        :param df: A pandas DataFrame that is to be processed.
        :type df: pd.DataFrame
        :return: A new pandas DataFrame with updated column data types as per
                 the mapping.
        :rtype: pd.DataFrame
        """
        dtype_names: List[str] = df.dtypes.astype(str).tolist()
        target_dtype_names = self._map_dtype_names(dtype_names)
        col_to_dtype = dict(zip(df.columns, target_dtype_names))

        new_df = pd.DataFrame(df.values, columns=df.columns, dtype="object").fillna(np.nan).astype(col_to_dtype)
        return new_df

    def _target_dtype_name(self, dtype_name: str) -> str:
        if "pyarrow" not in dtype_name:
            return dtype_name

        if "bool" in dtype_name:
            return "bool"
            
        # Handle nested types
        if "list[pyarrow]" in dtype_name or "struct[pyarrow]" in dtype_name or "map[pyarrow]" in dtype_name:
            return "object"

        return self._mapper.get(dtype_name, self._default_target_type)

    def _map_dtype_names(self, dtype_names: List[str]) -> List[str]:
        return [self._target_dtype_name(dtype_name) for dtype_name in dtype_names]
