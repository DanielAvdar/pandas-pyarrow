from pandas_pyarrow.mappers import create_mapper, mapper_db_types, reverse_create_mapper

import pandas as pd
import pytest


# Define nested types to skip in tests
NESTED_TYPES = ["list[pyarrow]", "struct[pyarrow]", "map[pyarrow]"]


@pytest.mark.parametrize(
    "str_types",
    [
        (set(create_mapper().keys()) - set(mapper_db_types.keys())),
        (set(reverse_create_mapper(adapter="tz=").values())),
        (set(create_mapper().values())),
        (set(reverse_create_mapper(adapter="tz=").keys())),
    ],
)
def test_str_dtypes(str_types):
    for t in str_types:
        # Skip nested types that pandas dtype cannot handle
        if any(nested_type in t for nested_type in NESTED_TYPES):
            continue
            
        pd_dtype = pd.api.types.pandas_dtype(t)
        if "pyarrow" not in t:
            assert str(pd_dtype) in str_types


@pytest.mark.parametrize(
    "str_types",
    [
        (set(create_mapper().keys()) - set(mapper_db_types.keys())),
        (set(reverse_create_mapper(adapter="tz=").values())),
    ],
)
def test_str_dtypes_numpy(str_types):
    for t in str_types:
        # Skip nested types that pandas dtype cannot handle
        if any(nested_type in t for nested_type in NESTED_TYPES):
            continue
            
        pd_dtype = pd.api.types.pandas_dtype(t)
        assert str(pd_dtype) in str_types


def test_str_dtypes_pyarrow():
    mapper_from_numpy = create_mapper()
    mapper_from_pyarrow = reverse_create_mapper(adapter="tz=")
    str_types = set(mapper_from_numpy.values()).union(set(mapper_from_pyarrow.keys()))
    for t in str_types:
        # Skip nested types that pandas dtype cannot handle
        if any(nested_type in t for nested_type in NESTED_TYPES):
            continue
            
        pd_dtype = pd.api.types.pandas_dtype(t)
        pd_dtype_repr = repr(pd_dtype)
        assert pd_dtype_repr in str_types
