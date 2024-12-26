from typing import Any

from pandas_pyarrow import convert_to_numpy
from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


def generate_test_case(
    case_name: str,
    data: list,
    col_dtype: Any,
):
    return Parametrization.case(
        name=case_name,
        df_data=pd.DataFrame({"test_column": data}, dtype=col_dtype),
    )


@Parametrization.autodetect_parameters()
@generate_test_case(
    "object case",
    ["test1", "test2", None],
    "object",
)
@generate_test_case(
    "object case",
    ["test1", "test2", None],
    "O",
)
@generate_test_case(
    "object case",
    ["test1", "test2", None],
    str,
)
@generate_test_case(
    "bytes case",
    [b"str1", b"str2", None],
    "bytes",
)
@generate_test_case(
    "bytes non utf-8 case",
    [b"\\ud800", b"\\x82\\x83", None],
    "str",
)
def test_object_types(
    df_data,
):
    sa = PandasArrowConverter()
    adf = sa(df_data)
    assert list(adf.dtypes)[0] == "string[pyarrow]"
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in repr(rdf.dtypes[0])
    assert "pyarrow" not in str(rdf.dtypes[0])
