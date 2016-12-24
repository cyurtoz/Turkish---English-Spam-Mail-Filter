from __future__ import print_function, division
import nltk
import os
import random
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify
import feedparser
import EnglishProcessor
import TurkishProcessor as tp
import util as util

 
def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r', encoding='utf-8', errors='ignore')
        a_list.append(f.read())
    f.close()
    return a_list
 
def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(sentence).encode('utf-8').decode())]
 
def get_features(text, setting, processor):
    if setting=='bow':
        return {word: count for word, count in Counter(processor.preprocess(text)).items() if processor.isStopWord(word) == False}
    else:
        return {word: True for word in processor.preprocess(text) if processor.isStopWord(word) == False}
 
def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    # initialise the training and test sets
    train_set, test_set = features[:train_size], features[train_size:]
    print ('Training set size = ' + str(len(train_set)) + ' emails')
    print ('Test set size = ' + str(len(test_set)) + ' emails')
    # train the classifier
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier
 
def evaluate(train_set, test_set, classifier):
    # check how the classifier performs on the training and test sets
    print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)))
    print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)))
    # check which words are most informative for the classifier
    classifier.show_most_informative_features(50)
 
if __name__ == "__main__":
    # initialise the data
    all_emails = []
    tr_emails = []
    #spam_en = util.extractEmlMails('/Users/cyurtoz/Downloads/SH/SA/20030228_spam_2/')
    #ham_en = util.parseTxtFiles('/Users/cyurtoz/Downloads/enron4/ham/')
    spam_tr = tp.parseTurkishFiles('/Users/cyurtoz/Workspace/turkish_english_spam_mail_filter/data/turkish/spam/Training_DB/')
    ham_tr = tp.parseTurkishFiles('/Users/cyurtoz/Workspace/turkish_english_spam_mail_filter/data/turkish/ham/Training_DB/')
    spam_tr_test = tp.parseTurkishFiles('/Users/cyurtoz/Workspace/turkish_english_spam_mail_filter/data/turkish/spam/Test_DB/')
    ham_tr_test = tp.parseTurkishFiles('/Users/cyurtoz/Workspace/turkish_english_spam_mail_filter/data/turkish/ham/Test_DB/')
    #all_emails = [(email, 'spam') for email in spam_en]
    #all_emails += [(email, 'ham') for email in ham_en]
    tr_emails += [(email, 'ham', 'tr') for email in ham_tr]
    tr_emails += [(email, 'spam', 'tr') for email in spam_tr]
    tr_emails += [(email, 'ham', 'tr') for email in ham_tr_test]
    tr_emails += [(email, 'spam', 'tr') for email in spam_tr_test]
    
    all_emails += tr_emails 
    
    random.shuffle(all_emails)
    print ('Corpus size = ' + str(len(all_emails)) + ' emails')
 
    # extract the features
    all_features = []
    tr_features = [(get_features(email, '', tp), label) for (email, label, lang) in tr_emails]
    all_features += tr_features
    print ('Collected ' + str(len(all_features)) + ' feature sets')
 
    # train the classifier
    train_set, test_set, classifier = train(all_features, 0.8)
 
    # evaluate its performance
    evaluate(train_set, test_set, classifier)