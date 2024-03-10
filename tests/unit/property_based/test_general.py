from pandas_pyarrow.pda_converter import PandasArrowConverter
from tests.unit.property_based.pb_sts import df_st

import hypothesis as hp


@hp.given(df=df_st())
@hp.settings(max_examples=500)
def test_dtypes_hp(df):
    df_copy = df.copy()
    sa = PandasArrowConverter()
    adf = sa(df)

    new_dtypes_names = [repr(i) for i in adf.dtypes.tolist()]
    assert all(
        ["[pyarrow]" in dtype in new_dtypes_names for dtype in new_dtypes_names]
    ), "Some dtypes are not converted"
    assert not df.equals(adf), "The original df has been modified"
    assert df.equals(df_copy), "The original df has been modified"
