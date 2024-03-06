from datetime import datetime

import pandas as pd
from parametrization import Parametrization
from pytz import timezone

from schemarrow.schema_arrow import SchemArrow


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="datetime case",
    df_data=pd.DataFrame(
        {"test_column": [datetime.now(), None]}, dtype="datetime64[ns]"
    ),
    expected_dtype="timestamp[ns][pyarrow]",
)
@Parametrization.case(
    name="datetime ms case",
    df_data=pd.DataFrame(
        {"test_column": [datetime.now(), None]}, dtype="datetime64[ms]"
    ),
    expected_dtype="timestamp[ms][pyarrow]",
)
def test_dt_types(df_data, expected_dtype):
    sa = SchemArrow()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype


@Parametrization.case(
    name="datetime timezone case",
    data=dict(
        data={"test_column": [datetime.now(timezone("US/Eastern")), None]},
        dtype="datetime64[ns, US/Eastern]",
    ),
    expected_dtype="timestamp[ns, tz=US/Eastern][pyarrow]",
)
@Parametrization.case(
    name="datetime timezone case UTC",
    data=dict(
        data={"test_column": [datetime.now(timezone("UTC")), None]},
        dtype="datetime64[ns, UTC]",
    ),
    expected_dtype="timestamp[ns, tz=UTC][pyarrow]",
)
def test_dt_tz_types(data, expected_dtype):
    df_data = pd.DataFrame(**data)
    sa = SchemArrow()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="timedelta case",
    df_data=pd.DataFrame(
        {"test_column": [pd.Timedelta("1 days"), None]}, dtype="timedelta64[ns]"
    ),
    expected_dtype="duration[ns][pyarrow]",
)
@Parametrization.case(
    name="timedelta hours case",
    df_data=pd.DataFrame(
        {"test_column": [pd.Timedelta("5 hours"), None]}, dtype="timedelta64[ns]"
    ),
    expected_dtype="duration[ns][pyarrow]",
)
@Parametrization.case(
    name="timedelta minutes case",
    df_data=pd.DataFrame(
        {"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[ns]"
    ),
    expected_dtype="duration[ns][pyarrow]",
)
@Parametrization.case(
    name="timedelta minutes in ms case",
    df_data=pd.DataFrame(
        {"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[ms]"
    ),
    expected_dtype="duration[ms][pyarrow]",
)
@Parametrization.case(
    name="timedelta minutes timezone case",
    df_data=pd.DataFrame(
        {"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[ns]"
    ),
    expected_dtype="duration[ns][pyarrow]",
)
def test_timedelta_types(df_data, expected_dtype):
    sa = SchemArrow()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
