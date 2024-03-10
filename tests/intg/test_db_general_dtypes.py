from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="DB Int64 case",
    df_data=pd.DataFrame(data={"col1": [1, 2, 3, None]}, dtype="Int64"),
    expected_dtype="int64[pyarrow]",
)
@Parametrization.case(
    name="DB Int32 case",
    df_data=pd.DataFrame(data={"col1": [1, 2, 3, None]}, dtype="Int32"),
    expected_dtype="int32[pyarrow]",
)
@Parametrization.case(
    name="DB Float64 case",
    df_data=pd.DataFrame(data={"col1": [1.0, 2.0, 3.0, None]}, dtype="Float64"),
    expected_dtype="float64[pyarrow]",
)
@Parametrization.case(
    name="DB Float32 case",
    df_data=pd.DataFrame(data={"col1": [1.0, 2.0, 3.0, None]}, dtype="Float32"),
    expected_dtype="float32[pyarrow]",
)
def test_db_general_dtypes(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
