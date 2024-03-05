from datetime import datetime

import pandas as pd
from parametrization import Parametrization

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

    assert adf.dtypes[0] == expected_dtype
