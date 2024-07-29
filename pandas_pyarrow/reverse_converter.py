import pandas as pd


def convert_to_numpy(df: pd.DataFrame) -> pd.DataFrame:
    cols = df.columns
    dtypes = df.dtypes
    df_ = df.copy()
    for col, dtype in zip(cols, dtypes):
        if repr(dtype).startswith("timestamp"):
            dt_format = "[" + repr(dtype).split("[")[1]
            df_[col] = df_[col].values.astype(f"datetime64{dt_format}")
        elif repr(dtype) == "halffloat[pyarrow]":
            df_[col] = df_[col].values.astype("float16")
        elif repr(dtype).startswith("duration"):
            td_format = "[" + repr(dtype).split("[")[1]
            df_[col] = df_[col].values.astype(f"timedelta64{td_format}")
        elif repr(dtype).startswith("string"):
            df_[col] = df_[col].values.astype("object")
    return df_.convert_dtypes()
