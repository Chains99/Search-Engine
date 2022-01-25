from nltk.util import print_string
import numpy as np
from validators import length
from vector import Vector
from data_utils import DataUtils
from text_preprocessing import TextPreprocessing
import math
class VectorialModel():
    def __init__(self, docs):
        self.docs = docs
        self.doc_tools = DataUtils(docs)
        self.w_d = self.doc_tools.weight(self.docs)
        self.vocabulary_len = self.doc_tools.vocab_len
        self.vect_norm = []
        for ds in self.w_d:
            self.vect_norm.append(self.norm(ds))
        
        
    def get_wd(self):
        for doc in self.docs:
            self.doc_tools.weight(doc)
    
    def dot(self, w1, w2):
        return w1@w2
  
    def norm(self, w):
        return np.linalg.norm(w)
   
    def doc_contain_query(self, doc_id ,query):
        for q in query[1]:
            if self.docs[doc_id + 1].__contains__(q):
                return True
        return False

    def query(self, text, k= 20):
        
        w_q = self.doc_tools.weight(text,is_query= True)
        rank = []
        self.index = 0
        self.qry_norm = self.norm(w_q[0])

        for ds in self.w_d:
            if self.doc_contain_query(self.index, text):
                rank.append([self.cosine_sim(ds, w_q[0]), self.index])
            self.index += 1

        rank = sorted(rank, reverse= True)
        return rank[: min(k, len(rank))]

    def cosine_sim(self, w1, w2):
        cos_sim = self.dot(w1, w2)/(self.vect_norm[self.index]*self.qry_norm)
        return cos_sim