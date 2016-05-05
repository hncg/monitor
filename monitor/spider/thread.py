# coding=utf-8
import threading
from .base import Base
from utils import do_time
from handler.model import Article

cityIdMap = {
	"长沙": 1
}
host = "http://bbs.rednet.cn/forum.php"
url_args = "?mod=forumdisplay&fid={fid}&filter=author&orderby=dateline&page={page}" # noqa


class MyThread(threading.Thread):

	def __init__(self, city, latest_time_at, tids):
		threading.Thread.__init__(self)
		self.city = city
		self.latest_time_at = latest_time_at or \
			do_time.str2datetime("1990-01-01 00:00", "%Y-%m-%d %H:%M")
		self.tids = tids

	def run(self):
		print self.city.name, "线程开始抓取"
		for i in xrange(1, 2):
			articles = []
			url = host + url_args.format(fid=str(self.city.fid), page=str(i))
			home_page = Base.get_home(url)
			article_infos = Base.get_article_infos(home_page)
			for article_info in article_infos:
				time_at = do_time.str2datetime(article_info['time_at'], "%Y-%m-%d %H:%M")
				tid = int(article_info['tid'])
				if time_at <= self.latest_time_at and article_info['_type'] != 'hot':
					Article.add_all(articles)
					print self.city.name, "结束"
					return
				else:
					if tid not in self.tids:
						print "抓取", self.city.name, i, "页", "帖子", article_info['title']
						content = Base.get_content(article_info['url'])
						articles.append(
							Article(
								city_id=self.city.id,
								tid=tid,
								type=article_info['_type'],
								title=article_info['title'],
								time_at=time_at,
								content=content,
								author=article_info['author'],
								reply_number=article_info['reply_number'],
								read_number=article_info['read_number'],
								url=article_info['url'],
							))
			Article.add_all(articles)
		print self.city.name, "结束"
