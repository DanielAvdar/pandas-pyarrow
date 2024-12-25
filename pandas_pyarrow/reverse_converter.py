# import pandas as pd
#
#
# def convert_to_numpy(df: pd.DataFrame) -> pd.DataFrame:
#     cols = df.columns
#     dtypes = df.dtypes
#     df_ = df.copy()
#     for col, dtype in zip(cols, dtypes):
#         if repr(dtype).startswith("timestamp"):
#             dt_format = "[" + repr(dtype).split("[")[1]
#             df_[col] = df_[col].values.astype(f"datetime64{dt_format}")
#         elif repr(dtype).startswith("halffloat"):
#             df_[col] = df_[col].values.astype("float16")
#         elif repr(dtype).startswith("duration"):
#             td_format = "[" + repr(dtype).split("[")[1]
#             df_[col] = df_[col].values.astype(f"timedelta64{td_format}")
#         elif repr(dtype).startswith("string"):
#             df_[col] = df_[col].values.astype("object")
#     return df_.convert_dtypes()
from pandas_pyarrow.mappers import reverse_create_mapper

import numpy as np
import pandas as pd

#
# def convert_to_numpy(df: pd.DataFrame) -> pd.DataFrame:
#     cols = df.columns
#     dtypes = df.dtypes
#     df_ = df.copy()
#     new_types = dict()
#     for col, dtype in zip(cols, dtypes):
#         if repr(dtype).startswith("timestamp"):
#             dt_format = "[" + repr(dtype).split("[")[1]
#             # df_[col] = df_[col].values.astype(f"datetime64{dt_format}")
#             new_types[col] = f"datetime64{dt_format}"
#         elif repr(dtype).startswith("halffloat"):
#             # df_[col] = df_[col].values.astype("float16")
#             new_types[col] = "float16"
#         elif repr(dtype).startswith("duration"):
#             td_format = "[" + repr(dtype).split("[")[1]
#             # df_[col] = df_[col].values.astype(f"timedelta64{td_format}")
#             new_types[col] = f"timedelta64{td_format}"
#         elif repr(dtype).startswith("string"):
#             # df_[col] = df_[col].values.astype(object)
#             new_types[col] = "object"
#     # return df_.convert_dtypes()
#     return df_.astype(new_types)#.convert_dtypes()
# def _target_dtype_name( dtype_name: str,type_mapper:dict[]) -> str:
#
# return type_mapper.get(dtype_name, "object")


def convert_to_numpy(df: pd.DataFrame) -> pd.DataFrame:
    values = df.values
    r_mapper = reverse_create_mapper()
    pyarrow_types = df.dtypes
    numpy_types = dict()
    for col, dtype in pyarrow_types.items():
        if "pyarrow" in repr(dtype):
            numpy_types[col] = r_mapper[repr(dtype)] if "bool" not in repr(dtype) else bool

        else:
            numpy_types[col] = dtype

    new_df = pd.DataFrame(values, columns=df.columns, dtype=object).fillna(np.nan).astype(numpy_types)
    return new_df
