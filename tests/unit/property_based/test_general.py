import hypothesis as hp

from schemarrow.schema_arrow import SchemArrow
from tests.unit.property_based.pb_sts import df_st


@hp.given(df=df_st())
@hp.settings(max_examples=500)
def test_dtypes_hp(df):
    sa = SchemArrow()
    adf = sa(df)

    new_dtypes_names = [repr(i) for i in adf.dtypes.tolist()]
    assert all(["[pyarrow]" in dtype in new_dtypes_names for dtype in new_dtypes_names])
