import math
from collections import Counter
import numpy as np
import math

a = 0.5

class DataUtils:
    def __init__(self, data):
        self.data = data
        self.data_len = len(self.data)
        self.terms_occurrences = self.term_occurrence(data)
        self.vocabulary = self.get_vocabulary()
        self.vocab_len = len(self.vocabulary)
        self.df_vals = self.df()

    def term_occurrence(self, text):
        freq = {}
        id = 1
        for data in text:
            for term in text[data]:
                try:
                    freq[term].add(id)
                except:
                    freq[term] = {id}

            id +=1

        for f in freq:
            freq[f] = len(freq[f])
            
        return freq

    def get_vocabulary(self):
        freq = self.terms_occurrences
        vocabulary = [term for term in freq]
        return vocabulary

    def tf_idf(self, text, is_qry):
        tf_vals = self.tf(text)
        tf_idf = {}
        id = 1
        for data in text:
            for term in text[data]:
                if is_qry:
                    if term not in self.vocabulary:
                        continue
                    df = self.df_vals[term]
                    tf_idf[id, term] = (a + (1 - a)*tf_vals[id,term])*df
                
                else:
                    tf_idf[id, term] = tf_vals[id, term]*self.df_vals[term]

                
            id += 1
        return tf_idf

    def tf(self, text):
        tf_vals = {}
        id = 1
        for data in text:
            counter = Counter(text[data])
            if len(counter) == 0:
                id+=1
                continue
            max_freq = max(counter.values())
            for term in text[data]:
                tf = counter[term]/max_freq
                tf_vals[id, term] = tf

            id+=1
    
        return tf_vals
        
    def df(self):
        ocrns = self.terms_occurrences
        df_vals = {}
        for term in self.vocabulary:
            df = np.log(self.data_len/ocrns[term])
            df_vals[term] = df
        
        return df_vals


    def weight(self, text, is_query= False):
        W = np.zeros((len(text), self.vocab_len))
        tf_idf_values = self.tf_idf(text, is_qry= is_query)

        for pair in tf_idf_values:
            W[pair[0]-1][self.vocabulary.index(pair[1])] = tf_idf_values[pair]

        return W
    
