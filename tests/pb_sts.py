from typing import Any

import pandas as pd
from hypothesis import strategies as st
from hypothesis.extra.pandas import columns, data_frames, range_indexes


@st.composite
def dtypes_st(draw) -> st.SearchStrategy[Any]:
    dtypes = st.sampled_from(
        [
            int,
            float,
            bool,
            str,
            "datetime64[ns]",
            "timedelta64[ns]",
            "timedelta64[ms]",
            "int8",
            "int16",
            "int32",
            "int64",
            "float16",
            "float32",
            "float64",
        ]
    )
    return draw(dtypes)


@st.composite
def df_st(draw) -> st.SearchStrategy[pd.DataFrame]:
    col_names = draw(st.sets(st.text(min_size=1, max_size=10), min_size=2, max_size=5))
    dfs_st = data_frames(
        columns=columns(
            list(col_names),
            dtype=draw(dtypes_st()),
        ),
        index=range_indexes(
            min_size=2,
            max_size=5,
        ),
    )
    df = draw(dfs_st)
    return df
