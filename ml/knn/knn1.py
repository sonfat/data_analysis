# -*- coding:utf-8 -*-

import sys
import urllib
import urlparse
import re
from hmmlearn import hmm
import numpy as np
from sklearn.externals import joblib
import HTMLParser
import nltk
import csv
import matplotlib.pyplot as plt
from nltk.probability import  FreqDist
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn import metrics

N = 100 #测试样本数

def load_user_cmd(filename):
    cmd_list = []
    dist_max = []
    dist_min = []
    dist = []
    with open(filename) as f:
        i = 0
        x = []
        for line in f:
            line = line.strip('\n')
            x.append(line)
            dist.append(line)
            i += 1
            if i == 100:
                x = []
                i = 0

    fdist = FreqDist(dist).keys()
    dist_max = set(fdist[0:50])
    dist_min = set(fdist[-50:0])
    return cmd_list, dist_max, dist_min

# test code
# test_text = "Sentiment analysis is a challenging subject in machine learning.People express their emotions in language that is often obscured by sarcasm,ambiguity, and plays on words, all of which could be very misleading for both humans and computers. There's another Kaggle competition for movie review sentiment analysis. In this tutorial we explore how Word2Vec can be applied to a similar problem.".lower()
test_text ="Sentiment analysis is a challenging subject in machine learning. \
People express their emotions in language that is often obscured by sarcasm, \
ambiguity, and plays on words, all of which could be very misleading for \
both humans and computers. There's another Kaggle competition for movie review \
sentiment analysis. In this tutorial we explore how Word2Vec can be applied to \
a similar problem.".lower()

english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
tmp_words = test_text.split(' ')
parse_word = []
# for word in test_text:
#     words.append(word)
for i in  tmp_words:
    if i