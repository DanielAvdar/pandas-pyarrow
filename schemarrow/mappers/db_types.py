from typing import Dict

mapper_db_types: Dict[str, str] = {
    "Int64": "int64[pyarrow]",
    "Int32": "int32[pyarrow]",
    "Int16": "int16[pyarrow]",
    "Int8": "int8[pyarrow]",
    "Float64": "float64[pyarrow]",
    "Float32": "float32[pyarrow]",
    "dbdate": "date32[pyarrow]",
    "dbtime": "time64[us][pyarrow]",
}
