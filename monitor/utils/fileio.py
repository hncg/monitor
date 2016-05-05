# coding=utf-8
import os


def mkdir(path):
    is_exists = os.path.exists(path)
    if not is_exists:   # 不存在目录
        os.makedirs(path)


def write(path, name, content, access_mode='w'):
    mkdir(path)
    fo = open(path + name, access_mode)
    if isinstance(content, unicode):
        content = content.encode('utf8')
    fo.write(content)
    fo.close()


def read(path, name):
    try:
        fo = open(path + name, 'r')
        _str = fo.read()
        fo.close()
        return _str.decode('utf8')
    except:
        return u""
