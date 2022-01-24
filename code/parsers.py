import os
import pandas as pd
import re
from collections import defaultdict


PATH_CRAN_TXT = 'TestCollections\Cranfield\cran.all.1400'
PATH_CRAN_QRY = 'TestCollections\Cranfield\cran.qry'
PATH_LISA = 'TestCollections\Lisa\LISA DOCS'
PATH_LISA_QRY = 'TestCollections\Lisa\LISA.QUE'

ID = re.compile('\.I')
doc_strip_pattern = re.compile('\n?Document {1,2}')
numeral_pattern = re.compile('#')

def get_data(path, sep):
    with open(path, 'r') as f:
        txt = f.read().replace('\n', " ")
        lns = re.split(sep, txt)
        if(lns[0] == ''): 
            lns.pop(0)
    return lns

cran_docs = get_data(PATH_CRAN_TXT, ID)
cran_qries = get_data(PATH_CRAN_QRY, ID)
lisa_qries = get_data(PATH_LISA_QRY, numeral_pattern)
lisa_qries.pop(len(lisa_qries) - 1)

cran_patterns = re.compile('\.[A,B,T,W]')

def cran_data_splitter(data, patterns, attributes: list):
    data_splter_dic = defaultdict(dict)
    for line in data:
        splted = re.split(patterns, line)
        id = int(splted[0].strip())
        index  = 1
        for atts in attributes:
            data_splter_dic[id][atts] = splted[index].strip()
            index += 1
    
    return data_splter_dic

cran_docs_list = cran_data_splitter(cran_docs, cran_patterns, ['title', 'author', 'references', 'text'])
cran_qries_list = cran_data_splitter(cran_qries, cran_patterns, ['question'])
lisa_docs_list = defaultdict(dict)
lisa_qries_list = defaultdict(dict)

lisa_docs_filenames = os.listdir(PATH_LISA)
lisa_txt_patterns = re.compile('  ')

def lisa_data_splitter(data, pattern, dict, attributes: list):
    for line in data:
        doc_splted = re.split(' ',line.strip(), maxsplit= 1)
        id = int(doc_splted[0].strip())
        index = 1
        if pattern is not None:
            doc_splted = re.split(pattern, doc_splted[1])
            index = 0

        for atts in attributes:
            dict[id][atts] = doc_splted[index].strip()
            index += 1
        
for filename in lisa_docs_filenames:
    data = get_data(PATH_LISA + '/' + filename, doc_strip_pattern)
    lisa_data_splitter(data, lisa_txt_patterns, lisa_docs_list, ['title', 'text'])

lisa_data_splitter(lisa_qries, None, lisa_qries_list, ['question'])
