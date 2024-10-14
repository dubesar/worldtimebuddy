import os
from typing import List
import datetime
import pytz

class DeltaValueError(Exception):
    """Custom exception for invalid delta format."""
    pass

def get_major_tz_from_env() -> List[str]:
    try:
        major_time_zones = os.environ.get("MAJOR_TIMEZONES", None)
        return list(major_time_zones[1:len(major_time_zones) - 1].split(','))
    except:
        return []

def callDelta(time: datetime.datetime, delta: str) -> datetime.datetime:
    """
    Apply a time delta to a given datetime object.

    Args:
        time (datetime.datetime): The original datetime object.
        delta (str): The time delta to apply (e.g., +2hr, -30min, -1day).

    Returns:
        datetime.datetime: The updated datetime object with the delta applied.

    Raises:
        DeltaValueError: If the delta format is invalid.
    """
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
        raise DeltaValueError("Invalid time format. Use +2hr, -30min, -1day, etc.")
    return time

def convert_timezone(time: datetime.datetime, target_timezone: str) -> datetime.datetime:
    """
    Convert a datetime object to a different timezone.

    Args:
        time (datetime.datetime): The original datetime object.
        target_timezone (str): The target timezone to convert to.

    Returns:
        datetime.datetime: The converted datetime object.

    Raises:
        pytz.exceptions.UnknownTimeZoneError: If the target timezone is unknown.
    """
    target_tz = pytz.timezone(target_timezone)
    return time.astimezone(target_tz)
