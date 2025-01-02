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
        name=f"test casting {source_dtype} to {target_dtype}",
        df_data=pd.DataFrame({"test_column": values}, dtype=source_dtype),
        expected_dtype=target_dtype,
    )


@Parametrization.autodetect_parameters()
@create_test_case("object", "string[pyarrow]", ["test1", "test2", None])
@create_test_case("O", "string[pyarrow]", ["test1", "test2", None])
@create_test_case(str, "string[pyarrow]", ["test1", "test2", None])
@create_test_case("bytes", "string[pyarrow]", [b"str1", b"str2", None])
@create_test_case(str, "string[pyarrow]", [b"\\ud800", b"\\x82\\x83", None])
@create_test_case("bool", "bool[pyarrow]", [True, False, None, True])
@create_test_case("boolean", "bool[pyarrow]", [True, False, None, True])
@create_test_case("bool", "bool[pyarrow]", [True, False, True])
@create_test_case("bool[pyarrow]", "bool[pyarrow]", [True, False, True])
@create_test_case("boolean", "bool[pyarrow]", [True, False, True])
@create_test_case(pd.BooleanDtype(), "bool[pyarrow]", [True, False, True])
@create_test_case("str", "string[pyarrow]", [True, False, None, True])
@create_test_case("<U1", "string[pyarrow]", [True, False, None, True])
@create_test_case("string", "string[pyarrow]", [True, False, None, True])
@create_test_case("category", "string[pyarrow]", [True, False, None, True])
@create_test_case("string[python]", "string[pyarrow]", [True, False, None, True])
@create_test_case("string[pyarrow]", "string[pyarrow]", [True, False, None, True])
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
