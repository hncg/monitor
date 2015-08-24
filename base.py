#coding=utf-8
import urllib2
import urllib
import re
import os
import sys 
import time
# reload(sys)  
# sys.setdefaultencoding('utf8')

class Base:
    def __init__(self,path='./',delay=0,large=0,detail=False,spiderAll=False):
        self.path = path
        self.delay = delay
        self.detail = detail
        self.spiderAll =spiderAll
        self.large = large

    def write(self,path,name,content):
        fo = open(path+name,'w')
        fo.write(content)
        fo.close()
    
    def read(self,path,name):
        fo = open(path+name,'r')
        str = fo.read()
        fo.close()
        return str
    def mkdir(self,path):
        isExists = os.path.exists(path)
        if not isExists:#不存在目录
            os.makedirs(path)
    def getPage(self,url,postdata=urllib.urlencode({})):
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20150727 Firefox/3.5.6'}
        if self.detail:
            httpHandler = urllib2.HTTPHandler(debuglevel=1)
            httpsHandler=urllib2.HTTPSHandler(debuglevel=1)
            opener=urllib2.build_opener(httpHandler,httpsHandler)
            urllib2.install_opener(opener)
        req = urllib2.Request(url)
        try:
            rep = urllib2.urlopen(req,postdata,timeout=10)
            page = rep.read()
        except:
            page = "self.path"+url
            print self.path,",线程网络发生错误,",self.delay,"秒之后重新抓取",url
            return self.delay
        page = page.decode('gb18030')
        page = page.encode('utf8')
        return page

    def getHomePage(self,url,name,postdata=urllib.urlencode({})):
        page = self.getPage(url)
        if page==self.delay:
            return page
        self.mkdir(self.path+'home/')
        self.getContents(page,name)
        self.write(self.path+'home/',name+'.html',page)

    def getContents(self,str1,pre_name):
        m =  re.search('<table summary=(.|\n)*</table><', str1)
        i=1
        self.mkdir(self.path+'title/')
        self.mkdir(self.path+'author/')
        self.mkdir(self.path+'read_number/')
        self.mkdir(self.path+'reply_number/')
        self.mkdir(self.path+'post_time/')
        self.mkdir(self.path+'reply_time/')
        self.mkdir(self.path+'link/')
        for m1 in re.finditer( '<tr>(.|\n)+?</tr>', m.group()):#得到包含标签 标题 时间 作者 最后一次评论时间 发表时间的内容的字符串 一共70条 m1.group(0)
            if len(m1.group())<=200:
                continue
            content = self.getContent(m1.group())
            self.write(self.path+'title/',pre_name+'_'+str(i)+'.html',content['title'])
            self.write(self.path+'author/',pre_name+'_'+str(i)+'.html',content['author'])
            self.write(self.path+'read_number/',pre_name+'_'+str(i)+'.html',content['read_number'])
            self.write(self.path+'reply_number/',pre_name+'_'+str(i)+'.html',content['reply_number'])
            self.write(self.path+'post_time/',pre_name+'_'+str(i)+'.html',content['post_time'])
            self.write(self.path+'reply_time/',pre_name+'_'+str(i)+'.html',content['reply_time'])
            self.write(self.path+'link/',pre_name+'_'+str(i)+'.html',content['link'])
            while True:
                    repeat = self.getDetail(detailUrl,int(pre_name),i)
                    if repeat == self.delay:#503错误出现,线程暂停delay秒
                            time.sleep(self.delay)
                            continue
                    else:
                        break
            print self.cityName,"第",pre_name,"页第",i,"条抓取完毕"
                
            i+=1

    def getContent(self,str1):#过滤出 标签 标题 时间 作者 最后一次评论时间 发表时间 等内容的字符串
        m =  re.search('http:(.|\n)+?html', str1)#链接
        link = m.group()
        content ={"link":link}
        m =  re.search('"xst"(.|\n)+?</a>', str1)#标题
        title = re.compile('"xst" >|</a>').sub('',m.group(0))
        content.setdefault("title",title)
        m =  re.search('c="1">(.|\n)+?</a>', str1)#作者
        author = re.compile('c="1">|</a>').sub('',m.group(0))
        content.setdefault("author",author)
        judge=1
        post_time = ""
        reply_time = ""
        for m in re.finditer( '>\d{4}-(.+?)</', str1):#发帖时间和最后回复时间
            if judge==1:
                post_time = re.compile('>|</').sub('',m.group(0)) 
                judge+=1
            else:
                reply_time = re.compile('>|</').sub('',m.group(0)) 
        content.setdefault("post_time",post_time)
        content.setdefault("reply_time",reply_time)

        m =  re.search('"xi2">(.*)</td>', str1)
        numbers = m.group(0)
        judge=1
        reply_number = ""
        read_number = ""
        for m in re.finditer( '>\d+', numbers):#帖子回复数量和浏览数量
            if judge==1:
                reply_number = re.compile('>').sub('',m.group(0))
                judge+=1
            else:
                read_number = re.compile('>').sub('',m.group(0))
        content.setdefault("reply_number",reply_number)
        content.setdefault("read_number",read_number)
        return content

    def getDetail(self,url,i,j,spiderAll=False):
        page = self.getPage(url)
        if page==self.delay:
            return page
        self.mkdir(self.path+'source_articel/')
        self.write(self.path+'source_articel/',str(i)+'_'+str(j)+'.html',page)
        for m in re.finditer('class="t_f"(.|\n)+?</td>', page):
            detail = re.compile(r'&nbsp;|\d+-\d+-\d+ \d+:\d+ 上传|下载附件|\(.*\)|<(.|\n)+?>').sub('','<'+m.group(0))
            self.mkdir(self.path+'articel/')
            self.write(self.path+'articel/',str(i)+'_'+str(j)+'.html',detail)
            if spiderAll == False:
                return 
