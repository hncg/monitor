#coding=utf-8
from base import * #阳 岳阳 益阳 常德 邵阳 娄底 永州 郴州 怀化 湘西 张家界 京沪江浙 粤港澳台
from Thread import *
city = {
        "雷明林":"http://dbsqp.com",
}
# print os.path.isfile('base1.py')
# page = bs.read('./长沙/home/',str(1)+".html")
today =datetime.date.today().strftime('%Y-%m-%d');
delay = 120
large =0
for x in city:
	while True:
		thread = threadTest(x+"详细",city[x],'./'+today+'/'+x,delay,large)
		thread.start()

"""
for i in range(1,101):
    strinfo = re.compile('\\d+.html')
    url = strinfo.sub(str(i)+".html",url)
    bs.write('./home/长沙/',str(i),bs.getPage(url,'',False))
"""
