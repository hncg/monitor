#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

list =jieba.lcut("我真是日了狗了")
for x in list:
    print x
