from datetime import datetime

from pandas_pyarrow import PandasArrowConverter, convert_to_numpy

import pandas as pd
from parametrization import Parametrization
from pytz import timezone


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
@Parametrization.case(
    name="Test Case: Datetime with UTC Timezone Seconds",
    data=dict(
        data={"test_column": [datetime.now(timezone("UTC")), None]},
        dtype="datetime64[s, UTC]",
    ),
    expected_dtype="timestamp[s, tz=UTC][pyarrow]",
)
def test_dt_tz_types(data, expected_dtype):
    df_data = pd.DataFrame(**data)
    sa = PandasArrowConverter()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in str(rdf.dtypes[0])
    assert rdf.compare(df_data).empty
