import db_dtypes as dbdt
import pandas as pd
from parametrization import Parametrization

from schemarrow.schema_arrow import SchemArrow


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="dbdate case",
    df_data=pd.DataFrame(
        data={"col1": [pd.Timestamp("2021-01-01"), None]}, dtype=dbdt.DateDtype()
    ),
    expected_dtype="date32[pyarrow]",
)
@Parametrization.case(
    name="dbtime case",
    df_data=pd.DataFrame(
        data={"col1": [pd.Timestamp("2021-01-01 12:00:00"), None]},
        dtype=dbdt.TimeDtype(),
    ),
    expected_dtype="time64[us][pyarrow]",
)
def test_db_date_dtypes(df_data, expected_dtype):
    sa = SchemArrow()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
