#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:16:55 2016

@author: cyurtoz
"""

from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
import util as util
import re
import Stemmer

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

stopwords = f = open("data/turkish/stoplist/turkce-stop-words",encoding="utf-8").read().split('\n')
def find_bigrams(word):
    token = nltk.word_tokenize(word)
    bigrams = ngrams(token,2)
    
def stem(word):
    return Stemmer.Stemmer('turkish').stemWord(word)
    
def parseTurkishFiles(folder):
    return util.parseTxtFiles(folder, 'ISO-8859-9')
    
def preprocess(sentence):
    wlist = []
    sentenceX =  word_tokenize(str(sentence).encode('utf-8').decode())
    for word in sentenceX:
        wordx = re.sub(r'\W+', '', stem(word.lower()))
        if (len(word) > 1):    
            wlist.append(wordx)
    return wlist
    

def isStopWord(word):
    return word in stopwords
 
    