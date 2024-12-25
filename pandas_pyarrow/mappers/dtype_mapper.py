from typing import Dict

mapper_dict_dt: Dict[str, str] = {
    "timedelta64[ns]": "duration[ns][pyarrow]",
    "timedelta64[ms]": "duration[ms][pyarrow]",
    "timedelta64[us]": "duration[us][pyarrow]",
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

reverse_mapper_dict: Dict[str, str] = {
    "duration[ns][pyarrow]": "timedelta64[ns]",
    "duration[ms][pyarrow]": "timedelta64[ms]",
    "duration[us][pyarrow]": "timedelta64[us]",
    "date32[pyarrow]": "date",
    # "timestamp[ns][pyarrow]": "timestamp",
    "string[pyarrow]": "object",
    "bool[pyarrow]": "bool",
    "time64[ns][pyarrow]": "datetime64[ns]",
    "time64[ms][pyarrow]": "datetime64[ms]",
    "time64[us][pyarrow]": "datetime64[us]",
    "double[pyarrow]": "float64",
    "float[pyarrow]": "float64",
    "halffloat[pyarrow]": "float16",
}
