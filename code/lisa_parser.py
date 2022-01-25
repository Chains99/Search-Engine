import os
import pandas as pd
import re
from collections import defaultdict

from validators.length import length


class LisaData:
    doc_strip_pattern = re.compile('\n?Document {1,2}')
    numeral_pattern = re.compile('#')
    lisa_txt_patterns = re.compile('  ')

    def __init__(self, path):
        self.path = path
        self.file_path = path
        

    def read_data(self, sep):
        with open(self.path, 'r') as f:
            txt = f.read().replace('\n', " ")
            lns = re.split(sep, txt)
            if(lns[0] == ''): 
                lns.pop(0)
        return lns

    def lisa_data_splitter(self, data, pattern, data_dict, attributes: list):
        for line in data:
            doc_splted = re.split(' ',line.strip(), maxsplit= 1)
            id = int(doc_splted[0].strip())
            index = 1
            if pattern is not None:
                doc_splted = re.split(pattern, doc_splted[1], maxsplit= 1)
                index = 0

            for atts in attributes:
                data_dict[id][atts] = doc_splted[index].strip()
                index += 1
    
    def get_data(self, attributes):
        if len(attributes) == 1:
            lisa_qries_list = defaultdict(dict)
            lisa_qries = self.read_data(self.numeral_pattern)
            lisa_qries.pop(len(lisa_qries) - 1)
            self.lisa_data_splitter(lisa_qries, None, lisa_qries_list, ['question'])
            return lisa_qries_list

        lisa_docs_filenames = os.listdir(self.path)
        lisa_docs_list = defaultdict(dict)
        for filename in lisa_docs_filenames:
            self.path = self.file_path + '/' + filename
            data = self.read_data(self.doc_strip_pattern)
            self.lisa_data_splitter(data, self.lisa_txt_patterns, lisa_docs_list, attributes)
            
        return lisa_docs_list











        



