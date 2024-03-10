from typing import Dict

import pytz


def datetime_mapper(from_type: str = "datetime64", to_type: str = "timestamp") -> Dict[str, str]:
    time_zones = pytz.all_timezones
    time_resolutions = ["ns", "ms", "us"]
    all_combinations = {f"{from_type}[{res}]": f"{to_type}[{res}][pyarrow]" for res in time_resolutions}
    all_tz_combinations = {
        f"{from_type}[{res}, {tz}]": f"{to_type}[{res}, {tz}][pyarrow]" for res in time_resolutions for tz in time_zones
    }
    all_combinations.update(all_tz_combinations)
    return all_combinations
