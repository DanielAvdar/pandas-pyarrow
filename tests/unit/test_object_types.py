import pandas as pd
from parametrization import Parametrization

from schemarrow.schema_arrow import SchemArrow


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="object case",
    df_data=pd.DataFrame({"test_column": ["test1", "test2", None]}, dtype="object"),
    expected_dtype="string[pyarrow]",
)
@Parametrization.case(
    name="bytes case",
    df_data=pd.DataFrame({"test_column": [b"str1", b"str2", None]}, dtype="bytes"),
    expected_dtype="string[pyarrow]",
)
def test_object_types(df_data, expected_dtype):
    sa = SchemArrow()
    adf = sa(df_data)

    assert list(adf.dtypes)[0] == expected_dtype
