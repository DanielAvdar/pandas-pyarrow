from pandas_pyarrow.mappers import create_mapper, reverse_create_mapper

import pandas as pd


def test_reverse_to_all_pyarrow_types():
    pyarrow_mapper = create_mapper()
    reverse_mapper = reverse_create_mapper(adapter="")
    all_pyarrow_types = set(pyarrow_mapper.values())
    all_reverse_types = set(reverse_mapper.keys())
    difference = all_pyarrow_types.difference(all_reverse_types)
    assert len(difference) == 0


def test_all_numpy_types():
    pyarrow_mapper = create_mapper()
    reverse_mapper = reverse_create_mapper(adapter="")
    all_source_numpy = set(pyarrow_mapper.keys())
    all_target_numpy = set(reverse_mapper.values())
    assert all_target_numpy.issubset(all_source_numpy)
    source_dtypes = {pd.api.types.pandas_dtype(t) for t in all_source_numpy if t not in {"dbtime", "dbdate"}}
    target_dtypes = {pd.api.types.pandas_dtype(t) for t in all_target_numpy}
    assert target_dtypes.issubset(source_dtypes)
