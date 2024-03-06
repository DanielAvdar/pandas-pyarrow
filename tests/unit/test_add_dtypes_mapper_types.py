from datetime import datetime

import pandas as pd
from parametrization import Parametrization

from schemarrow.schema_arrow import SchemArrow


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="test simple type mapping override with additional_mapper_dicts ns",
    df_data=pd.DataFrame(
        {"test_column": [datetime.now(), None]}, dtype="datetime64[ns]"
    ),
    expected_dtype="timestamp[ns,UTC][pyarrow]",
    additional_mapper_dicts={"datetime64[ns]": "timestamp[ns,UTC][pyarrow]"},
)
@Parametrization.case(
    name="test simple type mapping override with additional_mapper_dicts ms",
    df_data=pd.DataFrame(
        {"test_column": [datetime.now(), None]}, dtype="datetime64[ms]"
    ),
    expected_dtype="timestamp[ms,UTC][pyarrow]",
    additional_mapper_dicts={"datetime64[ms]": "timestamp[ms,UTC][pyarrow]"},
)
def test_add_dtypes_types(df_data, expected_dtype, additional_mapper_dicts):
    sa = SchemArrow(additional_mapper_dicts=additional_mapper_dicts)
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
