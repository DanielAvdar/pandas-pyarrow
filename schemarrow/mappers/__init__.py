from typing import Dict

from schemarrow.mappers.db_types import mapper_db_types
from schemarrow.mappers.dtype_mapper import (
    mapper_dict_dt,
    mapper_dict_numeric,
    mapper_dict_object,
)

all_mapper_dicts: Dict[str, str] = dict(
    **mapper_dict_numeric,
    **mapper_dict_dt,
    **mapper_dict_object,
    **mapper_db_types,
)
__all__ = [
    "mapper_dict_numeric",
    "mapper_dict_dt",
    "mapper_dict_object",
    "all_mapper_dicts",
    "mapper_db_types",
]
