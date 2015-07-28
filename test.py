#coding=utf-8
from base import *
bs = Base()
postdata=urllib.urlencode({
                'username':'aaa',
                'password':'why888',
                'continueURI':'http://www.verycd.com/',
                'fk':'',
                'login_submit':'bb'
        })
bs.write('./','test',bs.getPage("http://bbs.rednet.cn/forum-1757-1.html",postdata,False))
bs.getLink(bs.read('./','test'))
