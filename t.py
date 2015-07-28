import re

def dotest():
    line = "<a>aaaaa a</a><a>bbb   bvb</a><a>cc cc</a>llll</a>"
    for m in re.finditer( '<a>.*?</a>', line):
        print m.start(),m.group(0)
dotest()
