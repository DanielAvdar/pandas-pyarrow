# import pandas as pd
# from typing import Tuple
#
# import hypothesis as hp
#
# from pandas_pyarrow import convert_to_pyarrow
# from pandas_pyarrow.mappers import datetime_mapper
# from tests.unit.property_based.pb_sts import single_column_df_st
#
#
# @hp.given(
#     pair=single_column_df_st(
#         gen_type='datetime64[ns]',
#         pair_mapping=datetime_mapper(
#         )
#
#     )
# )
# def test_datetime_numpy_api_hp(pair: Tuple[pd.DataFrame, str]):
#     df, target_dtype = pair
#     adf = convert_to_pyarrow(df)
#
#     assert list(adf.dtypes)[0] == target_dtype
