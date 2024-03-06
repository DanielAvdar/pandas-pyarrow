import dataclasses
from typing import Dict, List

import pytz


@dataclasses.dataclass
class DateTimeMapper:
    source_type: str = "datetime64"
    target_type: str = "timestamp"
    symmetric: bool = True

    @property
    def timezones(self) -> List[str]:
        return pytz.all_timezones

    @property
    def time_resolutions(self) -> List[str]:
        return ["ns", "ms", "us"]

    @property
    def all_time_res_combs(self) -> Dict[str, str]:
        return {
            f"{self.source_type}[{res}]": f"{self.target_type}[{res}][pyarrow]"
            for res in self.time_resolutions
        }

    @property
    def all_time_res_tz_combs(self) -> Dict[str, str]:
        if not self.symmetric:
            return {
                f"{self.source_type}[{res}, {tz}]": f"{self.target_type}[{res}, {tz}][pyarrow]"
                for res in self.time_resolutions
                for tz in self.timezones
            }
        return {
            f"{self.source_type}[{res}, {tz}]": f"{self.target_type}[{res}][pyarrow]"
            for res in self.time_resolutions
            for tz in self.timezones
        }

    def __call__(
        self,
    ) -> Dict[str, str]:
        all_combinations = {**self.all_time_res_combs, **self.all_time_res_tz_combs}
        return all_combinations
