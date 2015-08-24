#coding=utf-8
from base import * #阳 岳阳 益阳 常德 邵阳 娄底 永州 郴州 怀化 湘西 张家界 京沪江浙 粤港澳台
from Thread import *
city = {
        "长沙":"http://bbs.rednet.cn/forum-1757-2.html",
         "株洲":"http://bbs.rednet.cn/forum-68-1.html",
         "湘潭":"http://bbs.rednet.cn/forum-69-1.html",
         "衡阳":"http://bbs.rednet.cn/forum-70-1.html",
         "岳阳":"http://bbs.rednet.cn/forum-71-1.html",
         "益阳":"http://bbs.rednet.cn/forum-72-1.html",
         "常德":"http://bbs.rednet.cn/forum-73-1.html",
         "邵阳":"http://bbs.rednet.cn/forum-74-1.html",
         "娄底":"http://bbs.rednet.cn/forum-75-1.html",
         "永州":"http://bbs.rednet.cn/forum-76-1.html",
         "郴州":"http://bbs.rednet.cn/forum-77-1.html",
         "怀化":"http://bbs.rednet.cn/forum-78-1.html",
         "湘西":"http://bbs.rednet.cn/forum-79-1.html",
         "张家界":"http://bbs.rednet.cn/forum-80-1.html",
}
url = "http://bbs.rednet.cn/forum-1757-1.html"
# print os.path.isfile('base1.py')
# page = bs.read('./长沙/home/',str(1)+".html")
today =datetime.date.today().strftime('%Y-%m-%d')
delay = 120
large =2
for x in city:
    thread = threadHome(x+"详细",city[x],'./'+today+'/'+x,delay,large)
    thread.start()
