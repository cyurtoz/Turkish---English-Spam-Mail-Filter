#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:16:55 2016

@author: cyurtoz
"""

from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
import Util as util
import re
import Stemmer
import ZemberekLemmaClient as zmb
import EnglishProcessor as en
import nltk

stopwords =  open("data/turkish/stoplist/turkce-stop-words",encoding="utf-8").read().split('\n')
    
def stem(word):
    return Stemmer.Stemmer('turkish').stemWord(word)
    
def parseTurkishFiles(folder):
    files = util.parseTxtFiles(folder, 'ISO-8859-9')
    arr = [extractBodyOfTurkishMails(a) for a in files ]
    return arr
    
def preprocess(sentence, zemberek=False):
    sentenceX = ''
    wlist = []
    if zemberek == True:
        sentenceX = zmb.post(sentence)
        for n,i in enumerate(sentenceX):
            if i=='UNK':
                sentenceX[n]=Stemmer.Stemmer('turkish').stemWord(sentence[n])
    else :   
        sentenceX =  word_tokenize(str(sentence).encode('utf-8').decode())
    for word in sentenceX:
        wordx = stem(word.lower())
        wlist.append(wordx)
    return wlist

def isStopWord(word):
    return word in stopwords
 
def extractBodyOfTurkishMails(email):
    arr = email.split('\n')
    arrx = [a for a in arr if not a.startswith('Kime') | a.startswith('Kimden') | a.startswith('Konu') | (a=='')]
    return ''.join(map(str,arrx))