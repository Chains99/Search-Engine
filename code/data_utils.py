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
            for term in data:
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
        id = 0
        for data in text:
            for term in data:
                if is_qry:
                    tf_idf[id, term] = (a + (1 - a)*tf_vals[id,term])*self.df_vals[term]
                
                else:
                    tf_idf[id, term] = tf_vals[id, term]*self.df_vals[term]

                
            id += 1
        return tf_idf

    def tf(self, text):
        tf_vals = {}
        id = 0
        for data in text:
            counter = Counter(data)
            max_freq = max(counter.values())
            for term in counter.keys():
                tf = counter[term]/max_freq
                tf_vals[id, term] = tf

            id+=1
    
        return tf_vals
        
    def df(self):
        ocrns = self.terms_occurrences
        df_vals = {}
        for data in self.data:
            for term in data:
                df = np.log(self.data_len/ocrns[term])
                df_vals[term] = df
        
        return df_vals


    def weight(self, text, is_query= False):
        W = np.zeros((len(text), self.vocab_len))
        tf_idf_values = self.tf_idf(text, is_qry= is_query)

        for pair in tf_idf_values:
            W[pair[0]][self.vocabulary.index(pair[1])] = tf_idf_values[pair]

        return W
    

'''import math
from collections import Counter
import numpy as np
import math

a = 0.5

class DataUtils:
    def __init__(self, data):
        self.data = data
        self.data_len = len(self.data)
        self.terms_occurrences = self.term_occurrence()
        self.vocabulary = self.get_vocabulary()
        self.vocab_len = len(self.vocabulary)
        self.df_vals = np.zeros((self.vocab_len))

    def term_occurrence(self, text):
        freq = {}
        id = 1
        for data in text:
            for term in data:
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
        ocrns = self.terms_occurrences
        tf_idf = {}
        df_dict = {}
        id = 0
        for data in text:
            counter = Counter(data)
            max_freq = max(counter.values())
            for term in counter.keys():
                tf = counter[term]/max_freq
                df = np.log(self.data_len/ocrns[term])
                if is_qry:
                    tf_idf[id, term] = (a + (1 - a)*tf)*self.df_vals[term]
                else:
                    tf_idf[id, term] = tf*df

                df_dict[term] = df
            id += 1
        self.df_vals = df_dict
        return tf_idf

    

    def weight(self, text, is_query= False):
        W = np.zeros((self.data_len, self.vocab_len))
        tf_idf_values = self.tf_idf(text, is_qry= is_query)

        for pair in tf_idf_values:
            W[pair[0]][self.vocabulary.index(pair[1])] = tf_idf_values[pair]

        return W
    
    
        
'''