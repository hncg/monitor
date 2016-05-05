# coding=utf-8
from spider.thread import MyThread
from handler.model import (
    City,
    Article
)

# latest_time_ats = Article.get_latest_time_at()
if __name__ == '__main__':
    citys = City.mget()
    articles = Article.mget_latest_time_at()
    latest_time_at_map = {articles[1]: articles[0] for
                          articles in articles}
    for city in citys:
        tids = [int(tid[0]) for tid in Article.mget_tids_by_city_id(city.id)]
        MyThread(city, latest_time_at_map.get(city.id), tids).start()
