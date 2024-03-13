from typing import Dict

from .datetime_mapper import datetime_mapper
from .db_types import mapper_db_types
from .dtype_mapper import mapper_dict_dt, mapper_dict_object
from .numeric_mapper import numeric_mapper


def create_mapper() -> Dict[str, str]:
    all_mapper_dicts: Dict[str, str] = dict(
        **numeric_mapper(["float"], ["16", "32", "64"]),
        **numeric_mapper(["int"], ["8", "16", "32", "64"]),
        **numeric_mapper(["Float", "Int"], ["32", "64"]),
        **numeric_mapper(["uint"], ["8", "16", "32", "64"]),
        **datetime_mapper(),
        **mapper_dict_dt,
        **mapper_dict_object,
        **mapper_db_types,
    )
    return all_mapper_dicts


__all__ = [
    "mapper_dict_dt",
    "mapper_dict_object",
    "create_mapper",
    "mapper_db_types",
    "datetime_mapper",
    "numeric_mapper",
]
