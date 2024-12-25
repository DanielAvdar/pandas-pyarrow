from pandas_pyarrow import convert_to_numpy
from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


def generate_test_case(case_name: str, data: list, col_dtype: str, expected_dtype: str):
    return Parametrization.case(
        name=case_name, df_data=pd.DataFrame({"test_column": data}, dtype=col_dtype), expected_dtype=expected_dtype
    )


@Parametrization.autodetect_parameters()
@generate_test_case("object case", ["test1", "test2", None], "object", "string[pyarrow]")
@generate_test_case("bytes case", [b"str1", b"str2", None], "bytes", "string[pyarrow]")
@generate_test_case("bytes non utf-8 case", [b"\\ud800", b"\\x82\\x83", None], "str", "string[pyarrow]")
def test_object_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)
    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in repr(rdf.dtypes[0])
    assert "pyarrow" not in str(rdf.dtypes[0])
