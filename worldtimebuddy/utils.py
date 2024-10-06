import os
from typing import List
import datetime

def get_major_tz_from_env() -> List[str]:
    try:
        major_time_zones = os.environ.get("MAJOR_TIMEZONES", None)
        return list(major_time_zones[1:len(major_time_zones) - 1].split(','))
    except:
        return []

def callDelta(time: datetime.datetime, delta: str) -> datetime.datetime:
    if 'hr' in delta:
        hours = int(delta.replace('hr', ''))
        time += datetime.timedelta(hours=hours)
    elif 'min' in delta:
        minutes = int(delta.replace('min', ''))
        time += datetime.timedelta(minutes=minutes)
    elif 'day' in delta:
        days = int(delta.replace('day', ''))
        time += datetime.timedelta(days=days)
    else:
        raise ValueError("Invalid time format. Use +2hr, -30min, -1day, etc.")
    return time