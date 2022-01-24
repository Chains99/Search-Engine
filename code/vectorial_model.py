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
        

    def dot(self, w1, w2):
        doct = 0
        index = 0
        while index<self.vocabulary_len:
           doct += w1[index]*w2[index]
           index+=1
        
        return doct

    def norm(self, w):
        norm = 0
        for component in w:
            norm += component**2
        return math.sqrt(norm)
    
    def query(self, text, k= 10):
        
        w_q = self.doc_tools.weight(text,is_query= True)
        rank = []
        self.doc_id = 0
        for ds in self.w_d:
            rank.append([self.cosine_sim(ds, w_q[0]), self.doc_id])
            self.doc_id += 1

        rank = sorted(rank, reverse= True)
        return rank

    def cosine_sim(self, w1, w2):
        cos_sim = self.dot(w1, w2)/self.vect_norm[self.doc_id]*self.norm(w2)
        return cos_sim