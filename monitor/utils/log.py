# coding=utf-8
import time
from fileio import (
    mkdir,
    write
)
from do_time import (
    format_time,

)


def log(path='../logs/', message='', level='Warning'):
    mkdir(path)
    ctime = time.time()
    write(path + level + '/', format_time(ctime, "%Y-%m-%d"),
          format_time(ctime) + " " + message + "\r\n", 'a')
