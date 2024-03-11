from typing import Dict, List, Optional

from .mappers import create_mapper

import pandas as pd


class PandasArrowConverter:
    """PandasArrowConverter manages the conversion of Pandas DataFrame data types to Arrow data types.

    :param parquet_compatible: if True, column names will be converted to parquet compatible names. Default is False.
    **disclaimer**: not yet implemented
    :param custom_mapper: dictionary with key as the source data type and value as the target data type.
    Will override default mapping
    :param default_target_type: Optional string specifying the default data type to use if no mapping is found for a
    specific data type. Default is "string[pyarrow]".

    Methods
    -------
    - __call__(self, df: pd.DataFrame) -> pd.DataFrame: Converts the data types of the given Pandas DataFrame
     and returns the converted DataFrame.
    """

    def __init__(
        self,
        parquet_compatible: Optional[bool] = False,
        custom_mapper: Optional[Dict[str, str]] = None,
        default_target_type: Optional[str] = "string[pyarrow]",
    ):
        self.parquet_compatible = parquet_compatible
        self.additional_mapper_dicts = custom_mapper or {}
        self.defaults_dtype = default_target_type
        self._mapper = create_mapper() | self.additional_mapper_dicts

    def __call__(self, df: pd.DataFrame) -> pd.DataFrame:
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
