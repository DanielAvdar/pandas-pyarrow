# File: test_reverse_converter.py
from pandas_pyarrow import convert_to_numpy, convert_to_pyarrow

import numpy as np
import pandas as pd


def test_convert_timestamp():
    data = {
        "timestamp_col": pd.Series(
            pd.date_range("2000", periods=100, freq="D"),
        )
    }
    df = pd.DataFrame(data)
    adf = convert_to_pyarrow(df)
    rdf = convert_to_numpy(adf)
    r_dtype = rdf["timestamp_col"].dtype
    assert "pyarrow" not in repr(r_dtype)
    rdf = convert_to_numpy(adf)


def test_convert_halffloat():
    data = {"halffloat_col": pd.Series(np.random.rand(100), dtype="float16")}
    df = pd.DataFrame(data)
    adf = convert_to_pyarrow(df)
    rdf = convert_to_numpy(adf)
    r_dtype = rdf["halffloat_col"].dtype
    assert "pyarrow" not in repr(r_dtype)
    rdf = convert_to_numpy(adf)


def test_convert_duration():
    data = {"duration_col": pd.Series(pd.to_timedelta(np.arange(100), "D"), dtype="timedelta64[ns]")}
    df = pd.DataFrame(data)
    adf = convert_to_pyarrow(df)
    rdf = convert_to_numpy(adf)
    r_dtype = rdf["duration_col"].dtype
    assert r_dtype == "timedelta64[ns]"
    rdf = convert_to_numpy(adf)


def test_convert_string():
    data = {"string_col": pd.Series(["abc", "def", "ghi"], dtype="object")}
    df = pd.DataFrame(data)
    adf = convert_to_pyarrow(df)
    rdf = convert_to_numpy(adf)
    r_dtype = rdf["string_col"].dtype
    assert repr(r_dtype) != "string[pyarrow]"
    assert "pyarrow" not in repr(r_dtype)
    assert "pyarrow" not in str(r_dtype)
