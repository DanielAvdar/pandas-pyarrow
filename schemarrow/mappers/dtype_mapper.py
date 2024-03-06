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
