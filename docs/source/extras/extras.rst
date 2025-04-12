.. _extras:

Extras
======

BigQuery Integration
--------------------

`pandas-pyarrow` supports seamless integration with BigQuery, allowing explicit conversion between BigQuery-specific dtypes and PyArrow.

Install with the BigQuery extra:

.. code-block:: bash

    pip install pandas-pyarrow[bigquery]

Example:

.. code-block:: python

    import pandas_gbq as gbq
    from pandas_pyarrow import PandasArrowConverter

    query = "SELECT * FROM `bigquery-public-data.austin_311.311_service_requests` LIMIT 1000"
    df = gbq.read_gbq(query)

    converter = PandasArrowConverter()
    adf = converter(df)

    print("Original types:\n", df.dtypes, "\n\nPyArrow types:\n", adf.dtypes)

Output Example:

.. code-block::

    unique_key                               object
    complaint_description                    object
    source                                   object
    status                                   object
    status_change_date          datetime64[us, UTC]
    created_date                datetime64[us, UTC]
    last_update_date            datetime64[us, UTC]
    close_date                  datetime64[us, UTC]
    incident_address                         object
    street_number                            object
    street_name                              object
    city                                     object
    dtype: object

Converted PyArrow-backed DataFrame types:

.. code-block::

    unique_key                           string[pyarrow]
    complaint_description                string[pyarrow]
    source                               string[pyarrow]
    status                               string[pyarrow]
    status_change_date        timestamp[us, tz=UTC][pyarrow]
    created_date              timestamp[us, tz=UTC][pyarrow]
    last_update_date          timestamp[us, tz=UTC][pyarrow]
    close_date                timestamp[us, tz=UTC][pyarrow]
    incident_address                      string[pyarrow]
    street_number                         string[pyarrow]
    street_name                           string[pyarrow]
    city                                  string[pyarrow]
    dtype: object
