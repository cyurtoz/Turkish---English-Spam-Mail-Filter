#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:51:57 2016

@author: cyurtoz
"""
import os as os
import random
import emlparser

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
    return open(folder + file, 'r', encoding=enc)

def extractEmlMails(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r', encoding='ISO-8859-1', errors='ignore')
        fx = emlparser.extract(f, f.name)['text']
        a_list.append(fx)
        f.close()
    return a_list
