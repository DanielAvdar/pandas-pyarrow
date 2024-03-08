# import pandas as pd
# from typing import Tuple
#
# import hypothesis as hp
#
# from schemarrow import SchemArrow
# from schemarrow.mappers import DateTimeMapper
# from tests.unit.property_based.pb_sts import single_column_df_st
#
#
# @hp.given(
#     pair=single_column_df_st(
#         gen_type='datetime64[ns]',
#         pair_mapping=DateTimeMapper(
#             source_type=["datetime64", ],
#             variations=[],
#         )()
#
#     )
# )
# def test_datetime_numpy_api_hp(pair: Tuple[pd.DataFrame, str]):
#     sa = SchemArrow()
#     df, target_dtype = pair
#     adf = sa(df)
#
#     assert list(adf.dtypes)[0] == target_dtype
