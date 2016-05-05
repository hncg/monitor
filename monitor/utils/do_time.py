# coding=utf-8
import datetime
import time


def utc2datetime(t):
    return datetime.datetime.fromtimestamp(t)


def datetime2utc(dt):
    return time.mktime(dt.timetuple())


def str2datetime(date_str, format_str="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strptime(date_str, format_str)


def format_time(t, format_str="%Y-%m-%d %H:%M:%S"):
    return time.strftime(format_str, time.localtime(t))
