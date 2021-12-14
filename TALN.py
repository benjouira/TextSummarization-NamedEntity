import spacy
import re
import nltk
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# !python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")
# *****************************

text = open("TexteBrut-AResumer.txt", "r")
text  = str(text.read())
print(text)


text = text.lower()
text = re.sub('\s+', ' ', text).strip()
print(text)

# **************************
doc = nlp(text)

# split and tokenize to sentences 
sentences = doc.sents
i=1
tokenSentences={}
for sent in sentences:
    tokenSentences[i]=sent
    i=i+1
    
tokenSentences
