#coding=utf-8
from base import *
from Thread import *
import sys
import re
"""
delay 503错误时休眠的时间间隔
large 开启下一个线程的缓冲时间
"""

today =datetime.date.today().strftime('%Y-%m-%d')
delay = 120
large = 3
for x in city:
    thread = threadHome(x,city[x],'./'+today+'/'+x,delay, large)
    thread.start()
    time.sleep(large)