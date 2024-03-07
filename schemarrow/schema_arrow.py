from typing import Dict, List, Optional

import pandas as pd

from schemarrow.mappers import all_mapper_dicts


class SchemArrow:
    def __init__(
            self,
            parquet_compatible: Optional[bool] = False,
            custom_mapper: Optional[Dict[str, str]] = None,
    ):
        self.parquet_compatible = parquet_compatible
        self.additional_mapper_dicts = custom_mapper or {}

    def __call__(self, df: pd.DataFrame) -> pd.DataFrame:
        dtype_names: List[str] = df.dtypes.astype(str).tolist()
        target_dtype_names = self._map_dtype_names(dtype_names)

        adf = df.astype(dict(zip(df.columns, target_dtype_names)))

        return adf

    def _map_dtype_names(self, dtype_names: List[str]) -> List[str]:
        type_mapper = all_mapper_dicts | self.additional_mapper_dicts
        target_dtype_names = []
        for dtype_name in dtype_names:
            target_dtype_name = type_mapper[dtype_name]
            target_dtype_names.append(target_dtype_name)
        return target_dtype_names
