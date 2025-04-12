.. _usage:

Usage
=====

Basic Usage
-----------

To convert a pandas DataFrame to PyArrow-backed DataFrame:

.. code-block:: python

    import pandas as pd
    from pandas_pyarrow import convert_to_pyarrow

    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c'],
        'C': [1.1, 2.2, 3.3],
        'D': [True, False, True]
    })

    adf = convert_to_pyarrow(df)

    print(adf.dtypes)

Output:

.. code-block::

    A     int64[pyarrow]
    B    string[pyarrow]
    C    double[pyarrow]
    D      bool[pyarrow]
    dtype: object

Custom Mappings
---------------

To customize your dtype mappings:

.. code-block:: python

    from pandas_pyarrow import PandasArrowConverter

    converter = PandasArrowConverter(
        custom_mapper={'int64': 'int32[pyarrow]', 'float64': 'float32[pyarrow]'}
    )
    adf_custom = converter(df)

    print(adf_custom.dtypes)

Output:

.. code-block::

    A     int32[pyarrow]
    B    string[pyarrow]
    C     float[pyarrow]
    D      bool[pyarrow]
    dtype: object
