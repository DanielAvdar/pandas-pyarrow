from typing import Dict

mapper_dict_numeric: Dict[str, str] = {
    "int8": "int8[pyarrow]",
    "int16": "int16[pyarrow]",
    "int32": "int32[pyarrow]",
    "int64": "int64[pyarrow]",
    "float16": "float16[pyarrow]",
    "float32": "float32[pyarrow]",
    "float64": "float64[pyarrow]",
}
mapper_dict_dt: Dict[str, str] = {
    "datetime64[ns]": "timestamp[ns][pyarrow]",
    "timedelta64[ns]": "time64[ns][pyarrow]",
    "datetime64": "timestamp[ns][pyarrow]",
    "timedelta64": "time64[pyarrow]",
    "date": "date32[pyarrow]",
    "time": "time64[pyarrow]",
    "timestamp": "timestamp[ns][pyarrow]",
}
mapper_dict_object: Dict[str, str] = {
    "object": "string[pyarrow]",
    "O": "string[pyarrow]",
    "category": "string[pyarrow]",
    "string": "string[pyarrow]",
    "binary": "binary[pyarrow]",
    "bool": "bool[pyarrow]",
}
