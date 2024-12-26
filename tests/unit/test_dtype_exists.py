from pandas_pyarrow.mappers import create_mapper, mapper_db_types, reverse_create_mapper

import pandas as pd
import pytest


@pytest.mark.parametrize(
    "str_types",
    [
        (set(create_mapper().keys()) - set(mapper_db_types.keys())),
        (set(reverse_create_mapper(adapter="tz=").values())),
        (set(create_mapper().values())),
        (set(reverse_create_mapper(adapter="tz=").keys())),
    ],
)
def test_mapper_dtypes(str_types):
    for t in str_types:
        pd.api.types.pandas_dtype(t)
