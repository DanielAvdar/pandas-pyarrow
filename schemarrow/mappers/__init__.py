from typing import Dict

from schemarrow.mappers.datetime_mapper import DateTimeMapper
from schemarrow.mappers.db_types import mapper_db_types
from schemarrow.mappers.dtype_mapper import mapper_dict_dt, mapper_dict_object
from schemarrow.mappers.numeric_mapper import NumericTimeMapper

all_mapper_dicts: Dict[str, str] = dict(
    **NumericTimeMapper()(),
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
]
