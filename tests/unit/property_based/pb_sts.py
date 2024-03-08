from typing import Any, Dict, List, Tuple, Union

import pandas as pd
from hypothesis import strategies as st
from hypothesis.extra.pandas import columns, data_frames, range_indexes
from hypothesis.strategies import composite

# Introduced constants
DTYPES_SAMPLE: List[Union[type, str]] = [
    int,
    float,
    bool,
    str,
    "datetime64[ns]",
    "timedelta64[ns]",
    "int8",
    "int16",
    "int32",
    "int64",
    "float16",
    "float32",
    "float64",
]


@composite
def dtypes_st(draw: Any) -> Any:
    dtypes = st.sampled_from(DTYPES_SAMPLE)
    return draw(dtypes)


def create_dataframe(draw: Any, gen_type: str) -> pd.DataFrame:
    dfs_st = data_frames(
        columns=columns(
            1,
            dtype=gen_type,
        ),
        index=range_indexes(
            min_size=1,
            max_size=6,
        ),

    )
    df = draw(dfs_st)

    for c in list(df.columns):
        if df[c].dtype == 'object' or df[c].dtype == 'category' or df[c].dtype == 'string':
            df[c] = "df[c].str.replace('\\u', '')"
            df[c] = df[c].astype(st.sampled_from(['str', 'bytes', 'object', 'category']))

    return df


@composite
def df_st(draw: Any) -> pd.DataFrame:
    col_names = draw(st.sets(st.text(min_size=1, max_size=10), min_size=2, max_size=5))
    dfs_st = data_frames(
        columns=columns(
            col_names,
            dtype=draw(st.sampled_from(DTYPES_SAMPLE)),
        ),
        index=range_indexes(
            min_size=2,
            max_size=8,
        ),

    )
    return draw(dfs_st)


@composite
def single_column_df_st(
        draw: Any,
        pair_mapping: Dict[str, str],
        gen_type: str = '',
) -> Tuple[pd.DataFrame, str]:
    pair: Tuple[str, str] = draw(st.sampled_from(list(pair_mapping.items())))
    source_dtype_name, target_dtype_name = pair
    df = create_dataframe(draw, gen_type or source_dtype_name.lower())
    df: pd.DataFrame = df.astype(source_dtype_name)
    return df, target_dtype_name
