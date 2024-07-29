from typing import Any, Dict, List, Tuple, Union

import pandas as pd
from hypothesis import strategies as st
from hypothesis.extra.pandas import columns, data_frames, range_indexes
from hypothesis.strategies import composite

# Dtype convertable to pyarrow via pandas api
COMMON_DTYPES_SAMPLE: List[Union[type, str]] = [
    bool,
    str,
    int,
    "datetime64[ns]",
    "timedelta64[ns]",
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
]
# Dtype not convertable to pyarrow via pandas api (pyarrow.lib.ArrowNotImplementedError)
UNCOMMON_DTYPES_SAMPLE: List[Union[type, str]] = [
    float,
    "float16",
    "float32",
    "float64",
    "complex64",
    "complex128",
]


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
    df: pd.DataFrame = draw(dfs_st)

    return df


@composite
def df_st(draw: Any, dtypes: List[Any]) -> pd.DataFrame:
    col_names = draw(st.sets(st.text(min_size=1, max_size=10), min_size=2, max_size=5))

    dfs_st = data_frames(
        columns=columns(
            col_names,
            dtype=draw(st.sampled_from(dtypes)),
        ),
        index=range_indexes(
            min_size=2,
            max_size=8,
        ),
    )
    df: pd.DataFrame = draw(dfs_st)
    category_columns = df.select_dtypes(include=["object"]).columns
    df[category_columns] = "s58^D#ww)"
    object_types = ["object", "string", "bytes", "str", "category", "O"]
    df[category_columns] = df[category_columns].astype(draw(st.sampled_from(object_types)))
    return df


@composite
def single_column_df_st(
    draw: Any,
    pair_mapping: Dict[str, str],
    gen_type: str = "",
) -> Tuple[pd.DataFrame, str]:
    pair: Tuple[str, str] = draw(st.sampled_from(list(pair_mapping.items())))
    source_dtype_name, target_dtype_name = pair
    df = create_dataframe(draw, gen_type or source_dtype_name.lower())
    with_tz = ", " in source_dtype_name
    if with_tz:
        col = df.columns[0]
        df[col] = df[col].dt.tz_localize("UTC")
    df: pd.DataFrame = df.astype(source_dtype_name)
    return df, target_dtype_name
