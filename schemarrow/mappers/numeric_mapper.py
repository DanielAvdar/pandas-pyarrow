from typing import Dict, List


def numeric_mapper(source_types: List[str], variations: List[str]) -> Dict[str, str]:
    def get_mapping(source_types: List[str]) -> Dict[str, str]:
        return {
            f"{source_type}{var}": f"{source_type.lower()}{var}[pyarrow]"
            for source_type in source_types
            for var in variations
        }

    all_ints = get_mapping([source_type for source_type in source_types if "int" in source_type.lower()])
    all_floats = get_mapping([source_type for source_type in source_types if "float" in source_type.lower()])
    all_combinations = {**all_ints, **all_floats}

    return all_combinations
