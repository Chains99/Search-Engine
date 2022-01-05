import re
import nltk
from nltk.corpus import stopwords
stopwords=set(stopwords.words('english'))

class TextProccesing:

    #Function for removing emailids from text
    def remove_email(self,text):
        if text:
            text = text.lower()
            text = re.sub('([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})',' ',str(text))
        else:
            pass
        return text

    # Function for removing paper refrences from text e.g [19],[1a,2b] or [19,14,15]
    def remove_refrence(self,text):
        if text:
            text=text.lower()
            text = re.sub('\[\d+(,\s{0,}\d+){0,}\]','',str(text))   
        else:
            pass
        return text
