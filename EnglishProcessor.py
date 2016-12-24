#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:16:55 2016

@author: cyurtoz
"""

from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
import os
import util

stopWords = stopwords.words('english')

def isStopWord(word):
    return word in stopWords
    
def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(sentence).encode('utf-8').decode())]