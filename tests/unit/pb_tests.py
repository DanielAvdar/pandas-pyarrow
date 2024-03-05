import hypothesis as hp

from schemarrow.schema_arrow import SchemArrow
from tests.pb_sts import df_st


@hp.given(df=df_st())
def test_dtypes_st(df):
    sa = SchemArrow()
    adf = sa(df)

    new_dtypes_names = [repr(i) for i in adf.dtypes.tolist()]
    assert all(["[pyarrow]" in dtype in new_dtypes_names for dtype in new_dtypes_names])
