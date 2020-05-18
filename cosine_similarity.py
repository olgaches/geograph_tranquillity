#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances


my_dirpath = ''

landcover_class_list = ['broadleaved', 'coniferous', 'arable', 'grassland', 'urban', 'suburban']

words_all = []
for landcover_class in landcover_class_list:
    filename_input_text = landcover_class + '_all_count.csv'
    input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input_text), delimiter=':', encoding='latin1')

    for i in range(0, 50):
        word = input_text_Geograph["word"][i]
        word_count = input_text_Geograph["count"][i]
        words_all.append(word)

dictionary = set(words_all)

Y = []
for landcover_class in landcover_class_list:
    Y1 = []
    filename_input_text = landcover_class + '_all_count.csv'
    input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input_text), delimiter=':', encoding='latin1')
    length = input_text_Geograph.shape[0]
    dic = {}
    for i in range(0, length):
        word = input_text_Geograph["word"][i]
        word_count = input_text_Geograph["count"][i]
        dic[word] = word_count
    for word in dictionary:
        if word not in dic.keys():
            Y1.append(0)
        else:
            Y1.append(dic[word])

    Y.append(Y1)

cosine_sim = 1 - pairwise_distances(Y, metric='cosine')

for i, my_id in zip(cosine_sim, landcover_class_list):
    print i, my_id


