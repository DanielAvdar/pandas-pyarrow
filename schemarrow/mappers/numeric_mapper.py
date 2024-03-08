import dataclasses
from typing import Dict, List


@dataclasses.dataclass
class NumericTimeMapper:
    source_types: List[str] = dataclasses.field(default_factory=lambda: ["float", "int", "Float", "Int"])
    variations: List[str] = dataclasses.field(
        default_factory=lambda: [
            "8",
            "16",
            "32",
            "64",
        ]
    )

    @property
    def all_ints(self) -> Dict[str, str]:
        return {
            f"{source_type}{var}": f"{source_type.lower()}{var}[pyarrow]"
            for source_type in self.source_types
            for var in self.variations
        }

    @property
    def all_floats(self) -> Dict[str, str]:
        return {
            f"{source_type}{var}": f"{source_type.lower()}{var}[pyarrow]"
            for source_type in self.source_types
            for var in self.variations
        }

    def __call__(
        self,
    ) -> Dict[str, str]:
        all_combinations = {**self.all_ints, **self.all_floats}
        return all_combinations
