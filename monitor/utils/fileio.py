#coding=utf-8

def write(self,path,name,content):
    fo = open(path+name,'w')
    fo.write(content)
    fo.close()

def read(self,path,name):
    try:
        fo = open(path+name,'r')
        str = fo.read()
        fo.close()
        return str
    except:
        return ""
def mkdir(self,path):
    isExists = os.path.exists(path)
    if not isExists:#不存在目录
        os.makedirs(path)
