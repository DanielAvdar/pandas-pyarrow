from datetime import datetime

from pandas_pyarrow import convert_to_numpy
from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization
from pytz import timezone


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="Test Case: Datetime",
    df_data=pd.DataFrame({"test_column": [datetime.now(), None]}, dtype="datetime64[ns]"),
    expected_dtype="timestamp[ns][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Datetime Milliseconds",
    df_data=pd.DataFrame({"test_column": [datetime.now(), None]}, dtype="datetime64[ms]"),
    expected_dtype="timestamp[ms][pyarrow]",
)
def test_dt_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in str(rdf.dtypes[0])


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="Test Case: Datetime with Timezone US/Eastern",
    data=dict(
        data={"test_column": [datetime.now(timezone("US/Eastern")), None]},
        dtype="datetime64[ns, US/Eastern]",
    ),
    expected_dtype="timestamp[ns, tz=US/Eastern][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Datetime with Timezone Africa/Abidjan",
    data=dict(
        data={"test_column": [datetime.now(timezone("Africa/Abidjan")), None]},
        dtype="datetime64[ns, Africa/Abidjan]",
    ),
    expected_dtype="timestamp[ns, tz=Africa/Abidjan][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Datetime with UTC Timezone",
    data=dict(
        data={"test_column": [datetime.now(timezone("UTC")), None]},
        dtype="datetime64[ns, UTC]",
    ),
    expected_dtype="timestamp[ns, tz=UTC][pyarrow]",
)
def test_dt_tz_types(data, expected_dtype):
    df_data = pd.DataFrame(**data)
    sa = PandasArrowConverter()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in str(rdf.dtypes[0])


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="Test Case: Timedelta",
    df_data=pd.DataFrame({"test_column": [pd.Timedelta("1 days"), None]}, dtype="timedelta64[ns]"),
    expected_dtype="duration[ns][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Timedelta in Hours",
    df_data=pd.DataFrame({"test_column": [pd.Timedelta("5 hours"), None]}, dtype="timedelta64[ns]"),
    expected_dtype="duration[ns][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Timedelta in Minutes",
    df_data=pd.DataFrame({"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[ns]"),
    expected_dtype="duration[ns][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Timedelta Minutes in Milliseconds",
    df_data=pd.DataFrame({"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[ms]"),
    expected_dtype="duration[ms][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Timedelta Minutes with Timezone",
    df_data=pd.DataFrame({"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[ns]"),
    expected_dtype="duration[ns][pyarrow]",
)
def test_timedelta_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in str(rdf.dtypes[0])
    # assert "[" in str(rdf.dtypes[0])
