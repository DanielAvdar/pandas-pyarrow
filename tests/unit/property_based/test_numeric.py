from typing import Tuple

from pandas_pyarrow import convert_to_numpy, convert_to_pyarrow
from pandas_pyarrow.mappers import numeric_mapper
from tests.unit.property_based.pb_sts import single_column_df_st

import hypothesis as hp
import pandas as pd


@hp.given(
    pair=single_column_df_st(
        pair_mapping=numeric_mapper(
            source_types=[
                "float",
            ],
            variations=["16", "32", "64"],
        )
    )
)
def test_float_numpy_api_hp(pair: Tuple[pd.DataFrame, str]):
    df, target_dtype = pair
    adf = convert_to_pyarrow(df)

    assert list(adf.dtypes)[0] == target_dtype
    rdf = convert_to_numpy(adf)
    assert "Float" not in str(rdf.dtypes[0])
    assert "pyarrow" not in str(rdf.dtypes[0])
    assert df.equals(rdf)


@hp.given(
    pair=single_column_df_st(
        pair_mapping=numeric_mapper(
            source_types=[
                "Float",
            ],
            variations=["32", "64"],
        )
    )
)
def test_float_array_api_hp(pair: Tuple[pd.DataFrame, str]):
    df, target_dtype = pair
    adf = convert_to_pyarrow(df)

    assert list(adf.dtypes)[0] == target_dtype
    rdf = convert_to_numpy(adf)
    assert "Float" not in str(rdf.dtypes[0])
    assert "pyarrow" not in str(rdf.dtypes[0])


@hp.given(
    pair=single_column_df_st(
        pair_mapping=numeric_mapper(
            source_types=[
                "int",
                "uint",
            ],
            variations=["8", "16", "32", "64"],
        )
    )
)
def test_int_numpy_api_hp(pair: Tuple[pd.DataFrame, str]):
    df, target_dtype = pair
    adf = convert_to_pyarrow(df)

    assert list(adf.dtypes)[0] == target_dtype
    rdf = convert_to_numpy(adf)
    assert "Int" not in str(rdf.dtypes[0])
    assert "pyarrow" not in str(rdf.dtypes[0])
    assert df.equals(rdf)


@hp.given(
    pair=single_column_df_st(
        pair_mapping=numeric_mapper(
            source_types=[
                "Int",
                "UInt",
            ],
            variations=["8", "16", "32", "64"],
        )
    )
)
def test_int_array_api_hp(pair: Tuple[pd.DataFrame, str]):
    df, target_dtype = pair
    adf = convert_to_pyarrow(df)

    assert list(adf.dtypes)[0] == target_dtype
    rdf = convert_to_numpy(adf)
    assert "Int" not in str(rdf.dtypes[0])
    assert "pyarrow" not in str(rdf.dtypes[0])
