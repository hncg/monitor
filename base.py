import urllib2
import urllib
import re
class Base:
    def write(self,path,name,content):
        fo = open(path+name,'w')
        fo.write(content)
        fo.close()
    
    def read(self,path,name):
        fo = open(path+name,'r')
        str = fo.read()
        fo.close()
        return str

    def getPage(self,url,postdata=urllib.urlencode({}),detail=False):
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20150727 Firefox/3.5.6'}
        if detail:
            httpHandler = urllib2.HTTPHandler(debuglevel=1)
            httpsHandler=urllib2.HTTPSHandler(debuglevel=1)
            opener=urllib2.build_opener(httpHandler,httpsHandler)
            urllib2.install_opener(opener)
        req = urllib2.Request(url)
        rep = urllib2.urlopen(req)
        page = rep.read()
        return page

    def getLink(self,str1):
        for m in re.finditer( '<table summary=.*</table><', str1):
            print m.start(),m.group(0)

        for m in re.finditer( '<a.*?</a>', str1):
            print m.start(),m.group(0)