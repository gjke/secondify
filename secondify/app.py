from datetime import timedelta
import re

multiplier_dict = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 3600 * 24,
    "w": 3600 * 24 * 7,
    "y": 3600 * 24 * 365
}
class TimeRepresentation:
    def __init__(self, str):
        self.secs = self.parse(str)

    def parse(self, str):
        match = re.match("^([1-9]{1}\d*)([smhdwy]{1})", str)

        if match is None:
            raise Exception("The provided string is invalid")
            exit()
        
        howmany = int(match.group(1))
        multiplier = multiplier_dict[match.group(2)]
        return howmany * multiplier
    
    def milliseconds(self):
        return self.secs * 1000

    def seconds(self):
        return self.secs

    def minutes(self):
        return self.secs / 60.0

    def hours(self):
        return self.secs / 3600
    
    def days(self):
        return self.secs / 3600 / 24.0
    
    def weeks(self):
        return self.secs / 3600 / 24 / 7.0

    def years(self):
        return self.secs / 3600 / 24 / 365


def parse(str):
    return TimeRepresentation(str)
