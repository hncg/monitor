# coding=utf8
from datetime import datetime
import time


def datetime2utc(dt):
    return time.mktime(dt.timetuple())


def utc2datetime(utc):
    return datetime.fromtimestamp(utc)


def serialize_to(obj, tobj):
    tobj = tobj()
    for k, v in tobj.__dict__.iteritems():
        value = getattr(obj, k)
        print value
        if isinstance(value, datetime):
            value = datetime2utc(value)
        if isinstance(value, unicode):
            value = value.encode('utf8')
        setattr(tobj, k, value)
    return tobj
