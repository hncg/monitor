# coding=utf-8
# from utils import fileio
from . import MyRequest
import re


class Base(object):

    @classmethod
    def get_home(cls, url):
        return MyRequest().request(url)

    @classmethod
    def get_content(cls, url):
        content = ""
        for table in re.finditer(u'<td class="t_f"(.|\n)+?</td>', MyRequest().request(url)): # noqa
            content += table.group() + "______"
        reg_str = u'<strong.+?\.(jpg|jpeg)|<(.|\n)+?>|\(.+下载次数.+?\)|下载附件| \
            |\d+-\d+-\d+ \d+:\d+ +?上传|&nbsp;|保存到相册|发表于 \d+-\d+-\d+ \d+:\d+| \
            |\r\n|于 .+?编辑'
        return re.compile(reg_str).sub(u'', content)

    @classmethod
    def get_article_infos(cls, home_page):
        article_infos = []
        for table in re.finditer(u'<tbody id=(.|\n)+?</tbody', home_page):
            table = table.group()
            _type = re.search(u'id=".+?"', table).group()

            if u'stickthread' in _type:
                _type = "hot"
            elif u'normalthread' in _type:
                _type = "normal"
            else:
                continue
            title = re.search(u'class="xst" >.+?</a', table)
            title = re.compile(u'class="xst" >|</a').sub(u'', title.group())

            author = re.search(u'c="1">.+?</a', table)
            author = re.compile(u'c="1">|</a').sub(u'', author.group())

            time_at = re.search(u'\d+-\d+-\d+ \d+:\d+', table).group()

            reply_number = re.search(u'class="xi2">\d+?</a', table)
            reply_number = re.compile(u'class="xi2">|</a').sub(u'', reply_number.group()) # noqa

            read_number = re.search(u'<em>\d+?</em', table)
            read_number = re.compile(u'<em>|</em').sub(u'', read_number.group()) # noqa

            tid = re.search(u'tid=\d+', table)
            tid = re.compile(u'tid=').sub(u'', tid.group())

            url = re.search(u'http://.+?"', table).group()[:-1]
            url = re.compile(u'amp;').sub(u'', url)
            url = len(url) > 256 and url[:255] or url

            article_infos.append({
                "title": title,
                "author": author,
                "time_at": time_at,
                "reply_number": reply_number,
                "read_number": read_number,
                "tid": tid,
                "url": url,
                "_type": _type
            })
        return article_infos
