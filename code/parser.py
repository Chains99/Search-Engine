import os
import pandas as pd
import re
from collections import defaultdict

PATH_CRAN_TXT = 'TestCollections/Cranfield/cran.all.1400'
PATH_CRAN_QRY = 'TestCollections/Cranfield/cran.qry'

ID = re.compile('\.I')

def get_docs(path, sep):
    with open(path, 'r') as f:
        txt = f.read().replace('\n', " ")
        lns = re.split(sep, txt)
        lns.pop(0)
    return lns

txt_list = get_docs(PATH_CRAN_TXT, ID)

patterns = re.compile('\.[A,B,T,W]')
docs_list = defaultdict(dict)

for line in txt_list:
    splted = re.split(patterns, line)
    id = splted[0]
    title = splted[1]
    author = splted[2]
    references = splted[3]
    text = splted[4].strip()

    docs_list[id]['title'] = title
    docs_list[id]['author'] = author
    docs_list[id]['references'] = references
    docs_list[id]['text'] = text
    
print(len(docs_list)) 
a = 0