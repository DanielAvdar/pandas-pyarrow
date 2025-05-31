from pandas_pyarrow import convert_to_numpy
from pandas_pyarrow.pda_converter import PandasArrowConverter

import pandas as pd
import numpy as np
import pytest
from parametrization import Parametrization


def create_df(column_values, data_type=None):
    if data_type:
        return pd.DataFrame({"test_column": column_values}, dtype=data_type)
    return pd.DataFrame({"test_column": column_values})


@Parametrization.autodetect_parameters()
@Parametrization.case(
    name="test list type detection",
    df_data=create_df([[1, 2, 3], [4, 5], [6, 7, 8, 9]]),
    expected_dtype="list[pyarrow]",
    additional_mapper_dicts=None,
)
@Parametrization.case(
    name="test dict type detection",
    df_data=create_df([{'a': 1, 'b': 2}, {'c': 3}, {'d': 4, 'e': 5}]),
    expected_dtype="struct[pyarrow]",
    additional_mapper_dicts=None,
)
def test_nested_types(df_data, expected_dtype, additional_mapper_dicts):
    converter = PandasArrowConverter(custom_mapper=additional_mapper_dicts)
    adf = converter(df_data)
    
    # Check that converter properly registered the nested type
    assert converter.nested_type_registry['test_column'] == expected_dtype
    
    # Check that the nested_types_registry is stored in the DataFrame
    assert hasattr(adf, "_nested_types_registry")
    assert adf._nested_types_registry['test_column'] == expected_dtype
    
    # Use the getter method to verify the type
    nested_types = converter.get_nested_dtypes(adf)
    assert nested_types['test_column'] == expected_dtype
    
    # Convert back to numpy and verify it's still object type
    rdf = convert_to_numpy(adf)
    assert rdf.dtypes.iloc[0] == np.dtype('O')
    
    # Verify data is present and has the right shape
    assert len(rdf) == len(df_data)
    assert rdf.shape == df_data.shape