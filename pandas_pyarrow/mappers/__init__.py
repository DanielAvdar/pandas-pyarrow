from typing import Dict

from .datetime_mapper import datetime_mapper, reverse_datetime_mapper
from .db_types import mapper_db_types
from .dtype_mapper import mapper_dict_dt, mapper_dict_object, reverse_mapper_dict
from .nested_mapper import nested_mapper_dict, reverse_nested_mapper_dict
from .numeric_mapper import numeric_mapper, reverse_numeric_mapper


def create_mapper() -> Dict[str, str]:
    all_mapper_dicts: Dict[str, str] = dict(
        **numeric_mapper(["float"], ["16", "32", "64"]),
        **numeric_mapper(["int", "Int", "uint", "UInt"], ["8", "16", "32", "64"]),
        **numeric_mapper(["Float"], ["32", "64"]),
        **datetime_mapper(),
        **mapper_dict_dt,
        **mapper_dict_object,
        **mapper_db_types,
        **nested_mapper_dict,
    )
    return all_mapper_dicts


def reverse_create_mapper(
    adapter: str = "tz=",
) -> Dict[str, str]:
    all_mapper_dicts: Dict[str, str] = dict(
        **reverse_numeric_mapper(["float"], ["16", "32", "64"]),
        **reverse_numeric_mapper(["int"], ["8", "16", "32", "64"]),
        **reverse_numeric_mapper(["uint"], ["8", "16", "32", "64"]),
        **reverse_datetime_mapper(adapter=adapter),
        **reverse_mapper_dict,
        **reverse_nested_mapper_dict,
    )
    return all_mapper_dicts


__all__ = [
    "mapper_dict_dt",
    "mapper_dict_object",
    "create_mapper",
    "reverse_create_mapper",
    "mapper_db_types",
    "datetime_mapper",
    "numeric_mapper",
    "nested_mapper_dict",
    "reverse_nested_mapper_dict",
]
