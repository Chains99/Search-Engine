import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from textblob import Word
stop_words=set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
porter_stemmer = PorterStemmer()

class TextPreprocessing:
    def __init__(self):
        self.contractions_dict = { "ain't": "are not","'s":" is","aren't": "are not","can't": "can not","can't've": "cannot have",
        "'cause": "because","could've": "could have","couldn't": "could not","couldn't've": "could not have",
        "didn't": "did not","doesn't": "does not","don't": "do not","hadn't": "had not","hadn't've": "had not have",
        "hasn't": "has not","haven't": "have not","he'd": "he would","he'd've": "he would have","he'll": "he will",
        "he'll've": "he will have","how'd": "how did","how'd'y": "how do you","how'll": "how will","i'd": "i would",
        "i'd've": "i would have","i'll": "i will","i'll've": "i will have","i'm": "i am","i've": "i have",
        "isn't": "is not","it'd": "it would","it'd've": "it would have","it'll": "it will","it'll've": "it will have",
        "let's": "let us","ma'am": "madam","mayn't": "may not","might've": "might have","mightn't": "might not",
        "mightn't've": "might not have","must've": "must have","mustn't": "must not","mustn't've": "must not have",
        "needn't": "need not","needn't've": "need not have","o'clock": "of the clock","oughtn't": "ought not",
        "oughtn't've": "ought not have","shan't": "shall not","sha'n't": "shall not",
        "shan't've": "shall not have","she'd": "she would","she'd've": "she would have","she'll": "she will",
        "she'll've": "she will have","should've": "should have","shouldn't": "should not",
        "shouldn't've": "should not have","so've": "so have","that'd": "that would","that'd've": "that would have",
        "there'd": "there would","there'd've": "there would have",
        "they'd": "they would","they'd've": "they would have","they'll": "they will","they'll've": "they will have",
        "they're": "they are","they've": "they have","to've": "to have","wasn't": "was not","we'd": "we would",
        "we'd've": "we would have","we'll": "we will","we'll've": "we will have","we're": "we are","we've": "we have",
        "weren't": "were not","what'll": "what will","what'll've": "what will have","what're": "what are",
        "what've": "what have","when've": "when have","where'd": "where did",
        "where've": "where have","who'll": "who will","who'll've": "who will have","who've": "who have",
        "why've": "why have","will've": "will have","won't": "will not","won't've": "will not have",
        "would've": "would have","wouldn't": "would not","wouldn't've": "would not have","y'all": "you all",
        "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",
        "you'd": "you would","you'd've": "you would have","you'll": "you will","you'll've": "you will have",
        "you're": "you are","you've": "you have"}

    
    def expand_contractions(self, text):
        # Regular expression for finding contractions
        contractions_re = re.compile('(%s)' % '|'.join(self.contractions_dict.keys()))
        def replace(match):
            return self.contractions_dict[match.group(0)]
        return contractions_re.sub(replace, text)

    def to_lower(self,text):
        if text:
            return text.lower()

    def remove_punctuations(self, text):
        return "".join([' ' if x in string.punctuation else x for x in text])

    #Function for removing emailids from text
    def remove_email(self,text):
        if text:
            text = word_tokenize(text)
            return re.sub('([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})',' ',str(text))

    # Function for removing paper refrences from text e.g [19],[1a,2b] or [19,14,15]
    def remove_reference(self,text):
        if text:
            text= word_tokenize(text)
            return re.sub('\[\d+(,\s{0,}\d+){0,}\]','',str(text))   

    #Function for removing stopwords from text
    def remove_stopwords(self, text):
        if text:
            text= word_tokenize(text)
            return " ".join(filter(lambda x: x not in stop_words, text))

    '''
    #Funcion for lemmatize the text
    def lemmatize(self, text):
        if text:
            text= word_tokenize(text)
            lem = []
            for token in text:
                w1 = Word(token).lemmatize("n")
                w2 = Word(w1).lemmatize("v")
                w3 = Word(w2).lemmatize("a")
                lem.append(Word(w3).lemmatize())
            return lem
    
    '''
    
    def lemmatize(self, text):
        if text:
            text= word_tokenize(text)
            return " ".join([wordnet_lemmatizer.lemmatize(x) for x in text])

    def stemming(self, text):
        if text:
            text= word_tokenize(text)
            return " ".join([porter_stemmer.stem(x) for x in text])

    def clean_text(self,text):
        text=re.sub('\w*\d\w*','', text)
        text=re.sub('\n',' ',text)
        text=re.sub(r"http\S+", "", text)
        text=re.sub('[^a-z]',' ',text)
        return text

    def preprocess_text(self, text):
        text = self.to_lower(text)
        text = self.expand_contractions(text)
        text = self.remove_punctuations(text)
        text = self.remove_stopwords(text)
        text = self.clean_text(text)
        #text = self.remove_reference(text)
        #text = self.remove_email(text)
        #text = self.stemming(text)
        text = self.lemmatize(text)
        return text