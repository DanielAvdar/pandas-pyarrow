# pandas-pyarrow

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pandas-pyarrow)](https://pypi.org/project/pandas-pyarrow/)
[![version](https://img.shields.io/pypi/v/pandas-pyarrow)](https://img.shields.io/pypi/v/pandas-pyarrow)
[![License](https://img.shields.io/:license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![OS](https://img.shields.io/badge/ubuntu-blue?logo=ubuntu)
![OS](https://img.shields.io/badge/win-blue?logo=windows)
![OS](https://img.shields.io/badge/mac-blue?logo=apple)
[![Tests](https://github.com/DanielAvdar/pandas-pyarrow/actions/workflows/ci.yml/badge.svg)](https://github.com/DanielAvdar/pandas-pyarrow/actions/workflows/ci.yml)
[![Code Checks](https://github.com/DanielAvdar/pandas-pyarrow/actions/workflows/code-checks.yml/badge.svg)](https://github.com/DanielAvdar/pandas-pyarrow/actions/workflows/code-checks.yml)
[![codecov](https://codecov.io/gh/DanielAvdar/pandas-pyarrow/graph/badge.svg?token=N0V9KANTG2)](https://codecov.io/gh/DanielAvdar/pandas-pyarrow)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

`pandas-pyarrow` simplifies the conversion of pandas backend to pyarrow, allowing seamlessly switch to pyarrow pandas
backend.

## Get started:

### Installation

To install the package use pip:

```bash
pip install pandas-pyarrow
```

### Usage

```python
import pandas as pd

from pandas_pyarrow import convert_to_pyarrow

# Create a pandas DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.1, 2.2, 3.3],
    'D': [True, False, True]
})

# Convert the pandas DataFrame dtypes to arrow dtypes
adf: pd.DataFrame = convert_to_pyarrow(df)

print(adf.dtypes)
```

outputs:

```
A     int64[pyarrow]
B    string[pyarrow]
C    double[pyarrow]
D      bool[pyarrow]
dtype: object
```

Furthermore, it's possible to add mappings or override existing ones:

```python
import pandas as pd

from pandas_pyarrow import PandasArrowConverter

# Create a pandas DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.1, 2.2, 3.3],
    'D': [True, False, True]
})

# Instantiate a PandasArrowConverter object
pandas_pyarrow_converter = PandasArrowConverter(
    custom_mapper={'int64': 'int32[pyarrow]', 'float64': 'float32[pyarrow]'})

# Convert the pandas DataFrame dtypes to arrow dtypes
adf: pd.DataFrame = pandas_pyarrow_converter(df)

print(adf.dtypes)
```

outputs:

```
A     int32[pyarrow]
B    string[pyarrow]
C     float[pyarrow]
D      bool[pyarrow]
dtype: object
```

pandas-pyarrow also support db-dtypes used by bigquery python sdk:

```bash
pip install pandas-gbq
```

or

```bash
pip install pandas-pyarrow[bigquery]
```

```python
import pandas_gbq as gbq

from pandas_pyarrow import PandasArrowConverter

# Specify the public dataset and table you want to query
dataset_id = "bigquery-public-data"
table_name = "hacker_news.stories"

# Construct the query string
query = """
    SELECT * FROM `bigquery-public-data.austin_311.311_service_requests` LIMIT 1000
"""

# Use pandas_gbq to read the data from BigQuery
df = gbq.read_gbq(query)
pandas_pyarrow_converter = PandasArrowConverter()
adf = pandas_pyarrow_converter(df)
# Print the retrieved data
print(df.dtypes)
print(adf.dtypes)
```

outputs:

```
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
incident_zip                              Int64
county                                   object
state_plane_x_coordinate                 object
state_plane_y_coordinate                float64
latitude                                float64
longitude                               float64
location                                 object
council_district_code                     Int64
map_page                                 object
map_tile                                 object
dtype: object
unique_key                         string[pyarrow]
complaint_description              string[pyarrow]
source                             string[pyarrow]
status                             string[pyarrow]
status_change_date          timestamp[us][pyarrow]
created_date                timestamp[us][pyarrow]
last_update_date            timestamp[us][pyarrow]
close_date                  timestamp[us][pyarrow]
incident_address                   string[pyarrow]
street_number                      string[pyarrow]
street_name                        string[pyarrow]
city                               string[pyarrow]
incident_zip                        int64[pyarrow]
county                             string[pyarrow]
state_plane_x_coordinate           string[pyarrow]
state_plane_y_coordinate           double[pyarrow]
latitude                           double[pyarrow]
longitude                          double[pyarrow]
location                           string[pyarrow]
council_district_code               int64[pyarrow]
map_page                           string[pyarrow]
map_tile                           string[pyarrow]
dtype: object
```

## Purposes

- Simplify the conversion between pandas pyarrow and numpy backends.
- Allow seamlessly switch to pyarrow pandas backend, even for problematic dtypes such float16 or db-dtypes.
- dtype standardization for db-dtypes used by bigquery python sdk.


example:

```python
import pandas as pd

# Create a pandas DataFrame
df = pd.DataFrame({

    'C': [1.1, 2.2, 3.3],

}, dtype='float16')

df.convert_dtypes(dtype_backend='pyarrow')
```
will raise an error:
```
pyarrow.lib.ArrowNotImplementedError: Unsupported cast from halffloat to double using function cast_double
```
but with pandas-pyarrow:
```python
import pandas as pd

from pandas_pyarrow import convert_to_pyarrow

# Create a pandas DataFrame
df = pd.DataFrame({

    'C': [1.1, 2.2, 3.3],

}, dtype='float16')
adf = convert_to_pyarrow(df)
print(adf.dtypes)

```
outputs:
```
C    halffloat[pyarrow]
dtype: object
```


## Additional Information

When converting from higher precision numerical dtypes (like float64) to
lower precision (like float32), data precision might be compromised.
