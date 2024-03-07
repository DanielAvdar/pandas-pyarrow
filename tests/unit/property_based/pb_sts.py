from typing import Any, Dict, List, Tuple, Union

import pandas as pd
from hypothesis import strategies as st
from hypothesis.extra.pandas import columns, data_frames, range_indexes

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


@st.composite
def dtypes_st(draw: Any) -> st.SearchStrategy[Any]:
    dtypes = st.sampled_from(DTYPES_SAMPLE)
    return draw(dtypes)


def create_dataframe(draw: Any, gen_type: str, col_names: str) -> pd.DataFrame:
    dfs_st = data_frames(
        columns=columns(
            [col_names],
        ),
        index=range_indexes(
            min_size=1,
            max_size=6,
        ),
        dtype=gen_type,

    )
    return draw(dfs_st)


@st.composite
def df_st(draw: Any) -> st.SearchStrategy[pd.DataFrame]:
    col_names = draw(st.sets(st.text(min_size=1, max_size=10), min_size=2, max_size=5))
    dfs_st = data_frames(
        columns=columns(
            col_names,
        ),
        index=range_indexes(
            min_size=2,
            max_size=8,
        ),
        dtype=draw(st.sampled_from(DTYPES_SAMPLE)),

    )
    return draw(dfs_st)


@st.composite
def single_column_df_st(
        draw: Any,
        pair_mapping: Dict[str, str],
        gen_type: str,
) -> st.SearchStrategy[Tuple[pd.DataFrame, str]]:
    col_name = draw(st.text(min_size=1, max_size=10))
    pair: Tuple[str, str] = draw(st.sampled_from(list(pair_mapping.items())))
    source_dtype_name, target_dtype_name = pair
    df = create_dataframe(draw, gen_type, col_name)
    df: pd.DataFrame = df.astype(source_dtype_name)
    return df, target_dtype_name
