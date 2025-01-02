from pandas_pyarrow.mappers import reverse_create_mapper

import numpy as np
import pandas as pd


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
