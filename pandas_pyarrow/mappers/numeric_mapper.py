from typing import Callable, Dict, List


def create_type_variations(
    source_types: List[str], filter_func: Callable[[str], bool], variations: List[str]
) -> Dict[str, str]:
    filtered_types = [source_type for source_type in source_types if filter_func(source_type)]
    return {
        f"{source_type}{variation}": f"{source_type.lower()}{variation}[pyarrow]"
        for source_type in filtered_types
        for variation in variations
    }


def numeric_mapper(source_types: List[str], variations: List[str]) -> Dict[str, str]:
    all_ints = create_type_variations(source_types, lambda x: "int" in x.lower(), variations)
    all_floats = create_type_variations(source_types, lambda x: "float" in x.lower(), variations)
    all_combinations = {**all_ints, **all_floats}
    return all_combinations
