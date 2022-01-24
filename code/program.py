from cranfield_parser import *
from lisa_parser import *
from text_preprocessing import TextPreprocessing
from vectorial_model import VectorialModel

def run_program(query= None):
    #Cranfield Collection Paths
    PATH_CRAN_TXT = 'TestCollections\Cranfield\cran.all.1400'
    PATH_CRAN_QRY = 'TestCollections\Cranfield\cran.qry'

    #Get Cranfield's Documents
    cran_docs_data = CranfieldData(PATH_CRAN_TXT)
    cran_docs_atts = ['title', 'author', 'references', 'text']
    cran_docs_dict = cran_docs_data.get_data(cran_docs_atts)
    
    #Get Cranfield's Queries
    cran_qries_data = CranfieldData(PATH_CRAN_QRY)
    cran_qry_atts = ['question']
    cran_qries_dict = cran_qries_data.get_data(cran_qry_atts)

    '''
    #Lisa Collection Paths
    PATH_LISA = 'TestCollections\Lisa\LISA DOCS'
    PATH_LISA_QRY = 'TestCollections\Lisa\LISA.QUE'

    #Get Lisa's Documents
    lisa_docs_data = LisaData(PATH_LISA)
    lisa_docs_atts = ['title', 'text']
    lisa_docs_dict = lisa_docs_data.get_data(lisa_docs_atts)

    #Get Lisa's Queries
    lisa_qries_data = LisaData(PATH_LISA_QRY)
    lisa_qry_atts = ['question']
    lisa_qries_dict = lisa_qries_data.get_data(lisa_qry_atts)
    '''

    all_docs = get_all_data(cran_docs_dict)
    all_qries = get_all_data(cran_qries_dict)
    vector_model = VectorialModel(all_docs)
    if query is None:
        rank =  vector_model.query([all_qries[0]])
    else:
        rank =  vector_model.query(query)
    rel_docs = []
    for docs in rank:
        rel_docs.append(cran_docs_dict[docs[1]])
    return rel_docs

def get_all_data(data):
    all_data = list()
    preprocess = TextPreprocessing()
    for doc in data:
        docmt = ''
        for elemnt in data[doc]:
            docmt += data[doc][elemnt]
        if docmt != '':
            all_data.append(preprocess.preprocess_text(docmt))
    return all_data

