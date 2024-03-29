from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


def create_test_case(
    dtype_name,
    expected_dtype,
    values,
):
    return Parametrization.case(
        name=f"Case handling {dtype_name} data type",
        df_data=pd.DataFrame({"test_column": values}, dtype=dtype_name),
        expected_dtype=expected_dtype,
    )


@Parametrization.autodetect_parameters()
@create_test_case("int64", "int64[pyarrow]", [1, 2, 3])
@create_test_case("int32", "int32[pyarrow]", [1, 2, 3])
@create_test_case("float64", "float64[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("float32", "float32[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("float16", "float16[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("uint16", "uint16[pyarrow]", [1, 2, 3])
@create_test_case("complex64", "string[pyarrow]", [1, 2, 3])
@create_test_case("float32[pyarrow]", "float32[pyarrow]", [1.0, 2.0, 3.0, None])
def test_numeric_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)
    assert list(adf.dtypes)[0] == expected_dtype
