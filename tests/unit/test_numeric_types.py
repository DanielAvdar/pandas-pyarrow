from schemarrow.schema_arrow import SchemArrow

import pandas as pd
from parametrization import Parametrization


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="int64 case",
    df_data=pd.DataFrame(
        {
            "test_column": [
                1,
                2,
                3,
            ]
        },
        dtype="int64",
    ),
    expected_dtype="int64[pyarrow]",
)
@Parametrization.case(
    name="int32 case",
    df_data=pd.DataFrame(
        {
            "test_column": [
                1,
                2,
                3,
            ]
        },
        dtype="int32",
    ),
    expected_dtype="int32[pyarrow]",
)
@Parametrization.case(
    name="float64 case",
    df_data=pd.DataFrame({"test_column": [1.0, 2.0, 3.0, None]}, dtype="float64"),
    expected_dtype="float64[pyarrow]",
)
@Parametrization.case(
    name="float32 case",
    df_data=pd.DataFrame({"test_column": [1.0, 2.0, 3.0, None]}, dtype="float32"),
    expected_dtype="float32[pyarrow]",
)
def test_numeric_types(df_data, expected_dtype):
    sa = SchemArrow()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
