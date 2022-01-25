from sys import meta_path

from nltk import metrics
from cranfield_parser import *
from lisa_parser import *
from text_preprocessing import TextPreprocessing
from vectorial_model import VectorialModel


def initialize():

    global docmts
    global qries 
    global model
    global qrel
    #Cranfield Collection Paths
    PATH_CRAN_TXT = 'TestCollections\Cranfield\cran.all.1400'
    PATH_CRAN_QRY = 'TestCollections\Cranfield\cran.qry'
    PATH_CRAN_REL = 'TestCollections\Cranfield\cranqrel'
    #Get Cranfield's Documents
    cran_docs_data = CranfieldData(PATH_CRAN_TXT)
    cran_docs_atts = ['title', 'author', 'references', 'text']
    docmts = cran_docs_data.get_data(cran_docs_atts)
<<<<<<< HEAD
    qrel = cran_docs_data.read_rel_doc(PATH_CRAN_REL)
=======
    '''
>>>>>>> be652cb407c77c494d61d2af5ad02ff1daf1fd8a
    #Get Cranfield's Queries
    cran_qries_data = CranfieldData(PATH_CRAN_QRY)
    cran_qry_atts = ['question']
    cran_qry_dict = cran_qries_data.get_data(cran_qry_atts)
    '''
    
    #Lisa Collection Paths
    PATH_LISA = 'TestCollections\Lisa\LISA DOCS'
    PATH_LISA_QRY = 'TestCollections\Lisa\LISA.QUE'

    #Get Lisa's Documents
    lisa_docs_data = LisaData(PATH_LISA)
    lisa_docs_atts = ['title', 'text']
    docmts = lisa_docs_data.get_data(lisa_docs_atts)

    #Get Lisa's Queries
    lisa_qries_data = LisaData(PATH_LISA_QRY)
    lisa_qry_atts = ['question']
    lisa_qry_dict = lisa_qries_data.get_data(lisa_qry_atts)
    
    '''

    all_docs = get_all_data(docmts)
    qries = get_all_data(lisa_qry_dict)
    
    model =  VectorialModel(all_docs)
    metcs = metrics(qries)
    for p in metcs:
        print(metcs[p])
    

def run_program(query= None):
    prep_qry = {}
    if query is None:
        prep_qry[1] = qries[1]
        rank =  model.query(prep_qry)
    else:
        prep_qry[1] = TextPreprocessing().preprocess_text(query).split(' ')
        rank_ =  model.query(prep_qry)
        len_=len(rank_)
        rank=rank_[:min(len_,20)]
    rel_docs = []

    for docs in rank:
        id = docs[1] + 1
        rel_docs.append([id, docmts[id]])
    return [len_,rel_docs]

def get_all_data(data):
    all_data = {}
    preprocess = TextPreprocessing()
    for doc in data:
        docmt = ''
        for elemnt in data[doc]:
            docmt += data[doc][elemnt]
        if str.isspace(docmt):
            all_data[doc] = docmt.strip()
        else:
            all_data[doc] = preprocess.preprocess_text(docmt).split(' ')
            
    return all_data


def metrics(queries):
    metrics = {}
    ind_qrel = 1
    for id in queries:
        rel =  run_program(" ".join(queries[id]))
        docs = []
        for index in rel:
            docs.append(index[0])
        set1 = set(docs)
        set2 = set(qrel[ind_qrel])
        inters = set1 & set2 
        total_inter = len(inters)
        res = []
        prec = total_inter/len(rel) #precision
        recall = total_inter/len(qrel[ind_qrel])  #recall
        F1 = (2*prec*recall)/(1 if prec + recall == 0 else prec + recall)  #f-score
        metrics[ind_qrel] = [prec,recall,F1]
        ind_qrel+=1
    return metrics

    
        
