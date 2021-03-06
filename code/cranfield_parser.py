import os
from nbformat import read
import pandas as pd
import re
from collections import defaultdict


class CranfieldData:
    ID = re.compile('\.I')
    cran_patterns = re.compile('\.[A,B,T,W]')

    def __init__(self, path):
        self.path = path

    def read_rel_doc(self, path):
        rel_docs = {}
        with open(path, 'r') as f:
            rl = f.readlines()
            rel  = []
            index = 1
            for line in rl:
                spltd = line.split(' ')
                id = int(spltd[0])
                if index != id:
                    rel_docs[id-1] = rel
                    index+=1
                    rel = []
                    
                rel.append(int(spltd[1]))
        rel_docs[len(rel_docs) + 1] = rel 
        return rel_docs



    def read_data(self, sep):
        with open(self.path, 'r') as f:
            txt = f.read().replace('\n', " ")
            lns = re.split(sep, txt)
            lns.pop(0)
        return lns    

    def cran_data_splitter(self, data, patterns, data_dict, attributes: list):
        for line in data:
            splted = re.split(patterns, line)
            id = int(splted[0].strip())
            index  = 1
            for atts in attributes:
                data_dict[id][atts] = splted[index]
                index += 1


    def get_data(self, attributes):
        data_splter_dic = defaultdict(dict)
        cran_data = self.read_data(self.ID)
        self.cran_data_splitter(cran_data, self.cran_patterns, data_splter_dic, attributes)
        return data_splter_dic
