# coding=utf-8
"""
    delay 503错误时休眠的时间间隔
    large 开启下一个线程的缓冲时间
"""
# import time
# import datetime
from conf import config
# from .. import city


def start():

    ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
    today = datetime.date.today().strftime(ISOTIMEFORMAT)
    delay = 120
    large = 3
    for x in city:
        print 1
        # thread = threadHome(x,city[x],'./'+today+'/'+x,delay, large)
        # thread.start()
        print 1
        time.sleep(large)
