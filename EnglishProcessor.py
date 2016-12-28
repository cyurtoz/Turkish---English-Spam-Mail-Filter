#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:16:55 2016

@author: cyurtoz
"""

from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords

stopWords = stopwords.words('english') + ['com', 'http', 'net', 'cc', 'from', 'wrote']

def isStopWord(word):
    return word in stopWords 
    
def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(sentence).encode('utf-8').decode())]
    
def preprocessWord(word):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word.lower())