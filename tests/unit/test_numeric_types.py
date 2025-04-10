from pandas_pyarrow import convert_to_numpy
from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


def create_test_case(
    source_dtype,
    target_dtype,
    values,
):
    return Parametrization.case(
        # name=f"Case handling {dtype_name} data type to {expected_dtype}",
        name=f"test casting {source_dtype} to {target_dtype}",
        df_data=pd.DataFrame({"test_column": values}, dtype=source_dtype),
        expected_dtype=target_dtype,
    )


@Parametrization.autodetect_parameters()
@create_test_case("int8", "int8[pyarrow]", [1, 2, 3])
@create_test_case("int16", "int16[pyarrow]", [1, 2, 3])
@create_test_case("int32", "int32[pyarrow]", [1, 2, 3])
@create_test_case("int64", "int64[pyarrow]", [1, 2, 3])
@create_test_case("Int8", "int8[pyarrow]", [1, 2, 3])
@create_test_case("Int16", "int16[pyarrow]", [1, 2, 3])
@create_test_case("Int32", "int32[pyarrow]", [1, 2, 3])
@create_test_case("Int64", "int64[pyarrow]", [1, 2, 3])
@create_test_case("uint8", "uint8[pyarrow]", [1, 2, 3])
@create_test_case("uint16", "uint16[pyarrow]", [1, 2, 3])
@create_test_case("uint32", "uint32[pyarrow]", [1, 2, 3])
@create_test_case("uint64", "uint64[pyarrow]", [1, 2, 3])
@create_test_case("UInt8", "uint8[pyarrow]", [1, 2, 3])
@create_test_case("UInt16", "uint16[pyarrow]", [1, 2, 3])
@create_test_case("UInt32", "uint32[pyarrow]", [1, 2, 3])
@create_test_case("UInt64", "uint64[pyarrow]", [1, 2, 3])
@create_test_case("float16", "float16[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("float32", "float32[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("float64", "float64[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("Float32", "float32[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("Float64", "float64[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("complex64", "string[pyarrow]", [1, 2, 3])
@create_test_case("float32[pyarrow]", "float32[pyarrow]", [1.0, 2.0, 3.0, None])
@create_test_case("float64[pyarrow]", "float64[pyarrow]", [1.0, 2.0, 3.0, None])
def test_numeric_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)
    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "Float" not in str(rdf.dtypes[0])
    assert "Int" not in str(rdf.dtypes[0])
    assert "pyarrow" not in repr(rdf.dtypes[0])
    assert "pyarrow" not in str(rdf.dtypes[0])
    assert len(set(rdf.dtypes).union(set(adf.dtypes))) > 1
    is_lowercase_dtype = str(df_data.dtypes[0]).lower() == str(df_data.dtypes[0])
    is_not_complex = "complex" not in str(df_data.dtypes[0])
    is_not_pyarrow = "pyarrow" not in str(df_data.dtypes[0])
    if is_lowercase_dtype and is_not_complex and is_not_pyarrow:
        assert df_data.equals(rdf)
