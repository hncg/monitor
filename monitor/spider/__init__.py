# coding=utf-8
import requests
import time
from utils import (
    log
)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'} # noqa
COOKIE = {}


class MyRequest(object):

    def request(self, url, headers=headers, cookies={}):
        delay = 60
        while(True):
            try:
                r = requests.get(url, headers=headers, timeout=10)
            except:
                print "网络异常,休眠", delay, "秒"
                log.log(message=u"网络异常" + url)
                time.sleep(delay)
                delay += 60
                continue
            if self.is_valid(r):
                return self.convert_encode(r)
            elif r.status_code == 503:
                log.log(message=u"503 error " + url)
                time.sleep(60)
                continue
            return u""

    def convert_encode(self, r):
        if r.encoding and r.encoding.lower() == 'gbk':
            text = r.text
            text = text.encode('utf8')
            text = text.decode('utf8')
            return text
        r.encoding = 'utf8'
        return r.text

    def is_valid(self, r):
        if r.status_code == 200:
            return len(r.text) > 2048
        else:
            return

    def get_cookie(self, r):
        return {cookie.name: cookie.value for cookie in r.cookies}
