import datetime
import time

@classmethod
def fromtimestamp(cls, t):
    "Construct a date from a POSIX timestamp(like time.time())."
    y, m, d, hh, mm, ss, weekday, jday, dst = time.localtime(t)
    return cls(y, m, d)

@classmethod
def today(cls):
    "Construct a date from time.time()."
    t = time.time()
    return cls.fromtimestamp(t)
