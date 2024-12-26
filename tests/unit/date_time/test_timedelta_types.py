from pandas_pyarrow import PandasArrowConverter, convert_to_numpy

import pandas as pd
from parametrization import Parametrization


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
@Parametrization.case(
    name="Test Case: Timedelta Minutes in Microseconds",
    df_data=pd.DataFrame({"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[us]"),
    expected_dtype="duration[us][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Timedelta Minutes in Seconds",
    df_data=pd.DataFrame({"test_column": [pd.Timedelta("30 minutes"), None]}, dtype="timedelta64[s]"),
    expected_dtype="duration[s][pyarrow]",
)
def test_timedelta_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in str(rdf.dtypes[0])
    assert rdf.compare(df_data).empty
    assert len(set(rdf.dtypes).union(set(adf.dtypes))) > 1
