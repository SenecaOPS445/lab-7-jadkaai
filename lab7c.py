#!/usr/bin/env python3
# Student ID: jkaai
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(t):
    """Convert time object to seconds"""
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    """Convert seconds to time object"""
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None
