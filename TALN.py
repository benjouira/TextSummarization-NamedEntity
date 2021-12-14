import spacy
import re
import nltk
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

# !python -m spacy download en_core_web_sm

# *****************************

text = open("TexteBrut-AResumer.txt", "r")
text  = str(text.read())
