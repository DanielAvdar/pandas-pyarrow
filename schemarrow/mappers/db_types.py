from typing import Dict

mapper_db_types: Dict[str, str] = {
    "dbdate": "date32[pyarrow]",
    "dbtime": "time64[us][pyarrow]",
}
