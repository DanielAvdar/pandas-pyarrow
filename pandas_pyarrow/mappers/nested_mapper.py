from typing import Dict

# Mapper for nested data types (lists and dictionaries)
# Only define the pyarrow type names, not the raw type names
nested_mapper_dict: Dict[str, str] = {}

# Maps pyarrow types back to pandas/numpy types
reverse_nested_mapper_dict: Dict[str, str] = {
    "list[pyarrow]": "object",
    "struct[pyarrow]": "object",
    "map[pyarrow]": "object",
}