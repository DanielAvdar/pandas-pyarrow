# reverse_converter.py

from typing import Dict, List, Optional

from .mappers import reverse_create_mapper

import numpy as np
import pandas as pd


class ReversePandasArrowConverter:
    def __init__(
        self,
        custom_mapper: Optional[Dict[str, str]] = None,
        default_target_type: Optional[str] = "object",
    ):
        self._mapper = reverse_create_mapper() | (custom_mapper or {})
        self._default_target_type = default_target_type

    def __call__(self, df: pd.DataFrame) -> pd.DataFrame:
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

        return self._mapper.get(dtype_name, self._default_target_type)

    def _map_dtype_names(self, dtype_names: List[str]) -> List[str]:
        return [self._target_dtype_name(dtype_name) for dtype_name in dtype_names]


def convert_to_numpy(df: pd.DataFrame) -> pd.DataFrame:
    """
    Legacy function for backward-compatibility.
    Instantiates ReversePandasArrowConverter and applies it.
    """
    converter = ReversePandasArrowConverter()
    return converter(df)
