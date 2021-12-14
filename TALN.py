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

# ********************************

# split to words
wordsSPACY = [word.text for word in doc]
print(wordsSPACY)

# *****************************
stopwords_spacy = list(STOP_WORDS)
punctuation

# ****************************
# Extract the lemma for each word
finalCleanText = " ".join([token.lemma_ for token in doc])
finalCleanText

# *************************
# convert the new lemma text from text type to nlp type
# to facilate the work later
doc = nlp(finalCleanText)

# ****************************

# calculat the frequencies of words without considerate the puncts and the stopwords
word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords_spacy:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text]=1
            else:
                word_frequencies[word.text]+=1

word_frequencies

# **************************************
# the most word exist
max_frequency = max(word_frequencies.values())
max_key = max(word_frequencies,key=word_frequencies.get)
print (max_key,' : ',max_frequency)
