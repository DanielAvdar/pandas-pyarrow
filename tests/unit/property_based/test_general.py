from pandas_pyarrow import convert_to_pyarrow
from tests.unit.property_based.pb_sts import COMMON_DTYPES_SAMPLE, UNCOMMON_DTYPES_SAMPLE, df_st

import hypothesis as hp


@hp.given(df=df_st(dtypes=COMMON_DTYPES_SAMPLE + UNCOMMON_DTYPES_SAMPLE))
def test_uncommon_dtypes_hp(df):
    df_copy = df.copy()
    adf = convert_to_pyarrow(df)

    new_dtypes_names = [repr(i) for i in adf.dtypes.tolist()]
    is_arrows = ["[pyarrow]" in dtype for dtype in new_dtypes_names]
    assert all(is_arrows), "Some dtypes are not converted"
    assert not df.equals(adf), "The original df has been modified"
    assert df.equals(df_copy), "The original df has been modified"
    assert adf.equals(convert_to_pyarrow(adf)), "The conversion is not idempotent"


@hp.given(df=df_st(dtypes=COMMON_DTYPES_SAMPLE))
def test_common_dtypes_hp(df):
    adf_pd_api = df.convert_dtypes(dtype_backend="pyarrow")
    adf = convert_to_pyarrow(df)
    assert adf_pd_api.compare(adf).empty, "The conversion is not consistent with pandas api"
