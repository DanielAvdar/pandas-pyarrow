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
    "datetime64[ms]": "timestamp[ms][pyarrow]",
    "datetime64[us]": "timestamp[us][pyarrow]",
    "timedelta64[ns]": "duration[ns][pyarrow]",
    "timedelta64[ms]": "duration[ms][pyarrow]",
    "timedelta64[us]": "duration[us][pyarrow]",
    "datetime64": "timestamp[ns][pyarrow]",
    "timedelta64": "duration[us][pyarrow]",
    "date": "date32[pyarrow]",
    "time": "timestamp[ns][pyarrow]",
    "timestamp": "timestamp[ns][pyarrow]",
}
mapper_dict_object: Dict[str, str] = {
    "object": "string[pyarrow]",
    "O": "string[pyarrow]",
    "category": "string[pyarrow]",
    "string": "string[pyarrow]",
    "bool": "bool[pyarrow]",
}
