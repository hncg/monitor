#coding=utf-8
import	threading
import	datetime
import	time
from base import * #阳 岳阳 益阳 常德 邵阳 娄底 永州 郴州 怀化 湘西 张家界 京沪江浙 粤港澳台
class threadHome(threading.Thread):#首页抓取线程

	def __init__(self, threadName, url, cityName, delay) :
		threading.Thread.__init__(self)
		self.threadName = threadName
		self.url = url
		self.cityName = cityName
		self.delay = delay

	def run(self):
		print self.threadName,"线程开始抓取"
		bs = Base(self.cityName+'/', self.delay)
		for i in xrange(1, 101) :
			homeUrl = re.compile('\\d+.html').sub(str(i)+".html", self.url)
			maxContinue = 100
			while True :
				conti = bs.getHomePage(homeUrl, str(i))
				if conti == self.delay :#503错误出现,线程暂停delay秒
					time.sleep(self.delay)
					maxContinue -= 1
					if maxContinue < 0 :
						bs.write('./', '503.log',detailUrl+'\n')
						break
					continue
				else :
					break
			print self.cityName, "第" , i , "页抓取完毕"
		print self.threadName, "结束"

class threadDetail(threading.Thread):#首页抓取线程
	def __init__(self, threadName, url, cityName, delay, large):
		threading.Thread.__init__(self)
		self.threadName = threadName
		self.url = url
		self.cityName = cityName
		self.delay = delay
		self.large = large

	def run(self):
		print self.threadName, "开始抓取"
		bs = Base(self.cityName+'/', self.delay, self.large, False, False)
		for i in xrange(1,101):
			for j in xrange(1,71):
				detailUrl = bs.read(self.cityName+"/link/", str(i) + "_" + str(j) + ".html")
				while True:
					repeat = bs.getDetail(detailUrl, i, j)
					if repeat == self.delay:#503错误出现,线程暂停delay秒
							time.sleep(self.delay)
							continue
					else:
						break
				print self.cityName , "第" , i , "页第" , j , "条抓取完毕"
		print self.cityName, "结束"

