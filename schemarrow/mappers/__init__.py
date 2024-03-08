from typing import Dict, List

from schemarrow.mappers.datetime_mapper import DateTimeMapper
from schemarrow.mappers.db_types import mapper_db_types
from schemarrow.mappers.dtype_mapper import mapper_dict_dt, mapper_dict_object
from schemarrow.mappers.numeric_mapper import NumericTimeMapper


def create_mapper_dict(source_types: List[str], variations: List[str]) -> Dict[str, str]:
    return NumericTimeMapper(
        source_types=source_types,
        variations=variations,
    )()


all_mapper_dicts: Dict[str, str] = dict(
    **create_mapper_dict(["float"], ["16", "32", "64"]),
    **create_mapper_dict(["int"], ["8", "16", "32", "64"]),
    **create_mapper_dict(["Float", "Int"], ["32", "64"]),
    **DateTimeMapper()(),
    **mapper_dict_dt,
    **mapper_dict_object,
    **mapper_db_types,
)

__all__ = [
    "mapper_dict_dt",
    "mapper_dict_object",
    "all_mapper_dicts",
    "mapper_db_types",
    "DateTimeMapper",
    "create_mapper_dict",
    "NumericTimeMapper",
]
