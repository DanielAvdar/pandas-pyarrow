from datetime import datetime

from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
from parametrization import Parametrization


def create_df(column_values, data_type):
    return pd.DataFrame({"test_column": column_values}, dtype=data_type)


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="test simple type mapping override with additional_mapper_dicts ns",
    df_data=create_df([datetime.now(), None], "datetime64[ns]"),
    expected_dtype="timestamp[ns,UTC][pyarrow]",
    additional_mapper_dicts={"datetime64[ns]": "timestamp[ns,UTC][pyarrow]"},
)
@Parametrization.case(
    name="test simple type mapping override with additional_mapper_dicts ms",
    df_data=create_df([datetime.now(), None], "datetime64[ms]"),
    expected_dtype="timestamp[ms,UTC][pyarrow]",
    additional_mapper_dicts={"datetime64[ms]": "timestamp[ms,UTC][pyarrow]"},
)
@Parametrization.case(
    name="test simple type mapping override with additional_mapper_dicts ms",
    df_data=create_df([0.0000000001, 2.0, 3.0, None], "float64"),
    expected_dtype="float32[pyarrow]",
    additional_mapper_dicts={"float64": "float32[pyarrow]"},
)
def test_add_dtypes_types(df_data, expected_dtype, additional_mapper_dicts):
    sa = PandasArrowConverter(custom_mapper=additional_mapper_dicts)
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
