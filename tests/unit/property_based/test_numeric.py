from typing import Tuple

import hypothesis as hp
import pandas as pd

from schemarrow import SchemArrow
from schemarrow.mappers import NumericTimeMapper
from tests.unit.property_based.pb_sts import single_column_df_st


@hp.given(
    pair=single_column_df_st(
        gen_type=float,
        pair_mapping=NumericTimeMapper(
            source_types=["float", ],
            variations=["16", "32", "64"],
        )()

    )
)
def test_float_numpy_api_hp(pair: Tuple[pd.DataFrame, str]):
    sa = SchemArrow()
    df, target_dtype = pair
    adf = sa(df)

    assert list(adf.dtypes)[0] == target_dtype


@hp.given(
    pair=single_column_df_st(
        gen_type=float,
        pair_mapping=NumericTimeMapper(
            source_types=["Float", ],
            variations=["32", "64"],
        )()

    )
)
def test_float_array_api_hp(pair: Tuple[pd.DataFrame, str]):
    sa = SchemArrow()
    df, target_dtype = pair
    adf = sa(df)

    assert list(adf.dtypes)[0] == target_dtype


@hp.given(
    pair=single_column_df_st(
        gen_type=int,
        pair_mapping=NumericTimeMapper(
            source_types=["int", ],
            variations=["8", "16", "32", "64"],
        )()

    )
)
def test_int_numpy_api_hp(pair: Tuple[pd.DataFrame, str]):
    sa = SchemArrow()
    df, target_dtype = pair
    adf = sa(df)

    assert list(adf.dtypes)[0] == target_dtype


@hp.given(
    pair=single_column_df_st(
        gen_type=int,
        pair_mapping=NumericTimeMapper(
            source_types=["Int", ],
            variations=["32", "64"],
        )()

    )
)
def test_int_array_api_hp(pair: Tuple[pd.DataFrame, str]):
    sa = SchemArrow()
    df, target_dtype = pair
    adf = sa(df)

    assert list(adf.dtypes)[0] == target_dtype
