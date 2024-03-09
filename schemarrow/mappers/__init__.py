from typing import Dict

from schemarrow.mappers.datetime_mapper import DateTimeMapper
from schemarrow.mappers.db_types import mapper_db_types
from schemarrow.mappers.dtype_mapper import mapper_dict_dt, mapper_dict_object
from schemarrow.mappers.numeric_mapper import numeric_mapper


def create_mapper() -> Dict[str, str]:
    all_mapper_dicts: Dict[str, str] = dict(
        **numeric_mapper(["float"], ["16", "32", "64"]),
        **numeric_mapper(["int"], ["8", "16", "32", "64"]),
        **numeric_mapper(["Float", "Int"], ["32", "64"]),
        **DateTimeMapper()(),
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
    "DateTimeMapper",
    "numeric_mapper",
]
