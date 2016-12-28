#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:51:57 2016

@author: cyurtoz
"""
import os as os
import random
import EmlParser as emlparser
import TurkishProcessor as tp
import EnglishProcessor as en
from collections import Counter

def parseTxtFiles(folder, enc):
    files = []
    file_list = os.listdir(folder)
    for file in file_list:
        f = openFile(folder, file, enc)
        files.append(f.read())
    f.close()
    return files

def randomize(emails):
    random.shuffle(emails)    
    
def openFile(folder, file, enc):
    return open(folder + file, 'r', encoding=enc, errors='ignore')

def extractEmlMails(folder):
    files = []
    file_list = os.listdir(folder)
    for file in file_list:
        f = extractEmlMail(folder, file, 'ISO-8859-1')
        files.append(f)
    return files
    
def extractEmlMail(folder, file, enc):
    f = openFile(folder, file, enc)
    fx = emlparser.extract(f, f.name)['text']
    f.close()
    return fx;

def find_bigrams(word):
    token = nltk.word_tokenize(word)
    return ngrams(token,2)

def isValidWord(word):
    return tp.isStopWord(word) == False and en.isStopWord(word) == False and word.isalpha() == True and len(word)>1
    
def extractFeatures(text, setting, processor):
    processed = processor.preprocess(text)
    if setting=='bow':
        return getFeaturesBow(processed)
    else:
        return getFeatures(processed)
        
def extractFeaturesWZemberek(text, setting, processor):
    processed = processor.preprocess(text, True)
    if setting=='bow':
        return getFeaturesBow(processed)
    else:
        return getFeatures(processed)
        
def getFeaturesBow(processed):
    return {word: count for word, count in Counter(processed).items() if isValidWord(word) == True}

def getFeatures(processed):
    return {word: True for word in processed if isValidWord(word) == True}
