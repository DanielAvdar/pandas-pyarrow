from datetime import datetime

from pandas_pyarrow import convert_to_numpy
from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="Test Case: Datetime",
    df_data=pd.DataFrame({"test_column": [datetime.now(), None]}, dtype="datetime64[ns]"),
    expected_dtype="timestamp[ns][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Datetime Milliseconds",
    df_data=pd.DataFrame({"test_column": [datetime.now(), None]}, dtype="datetime64[ms]"),
    expected_dtype="timestamp[ms][pyarrow]",
)
@Parametrization.case(
    name="Test Case: Datetime seconds",
    df_data=pd.DataFrame({"test_column": [datetime.now(), None]}, dtype="datetime64[s]"),
    expected_dtype="timestamp[s][pyarrow]",
)
def test_dt_types(df_data, expected_dtype):
    sa = PandasArrowConverter()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
    rdf = convert_to_numpy(adf)
    assert "pyarrow" not in str(rdf.dtypes[0])
    assert len(set(rdf.dtypes).union(set(adf.dtypes))) > 1
