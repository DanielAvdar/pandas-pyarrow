from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="Case handling integer 64 bit data type",
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
    name="Case handling integer 32 bit data type",
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
    name="Case handling floating point 64 bit data type",
    df_data=pd.DataFrame({"test_column": [1.0, 2.0, 3.0, None]}, dtype="float64"),
    expected_dtype="float64[pyarrow]",
)
@Parametrization.case(
    name="Case handling floating point 32 bit data type",
    df_data=pd.DataFrame({"test_column": [1.0, 2.0, 3.0, None]}, dtype="float32"),
    expected_dtype="float32[pyarrow]",
)
@Parametrization.case(
    name="Case handling PyArrow specific floating point 32 bit data type",
    df_data=pd.DataFrame({"test_column": [1.0, 2.0, 3.0, None]}, dtype="float32[pyarrow]"),
    expected_dtype="float32[pyarrow]",
)
def test_numeric_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)
    assert list(adf.dtypes)[0] == expected_dtype
