#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import codecs
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from my_functions import replace_encoding_stuff
import nltk
from nltk import word_tokenize
nltk.download('punkt')

my_dirpath = '//fs.geo.uzh.ch/ochesnok/documents/2_projects/11_tranquillity/corpus/'
filename_input = 'geograph_data/gridimage_text.tsv'

search_terms = ['tranquillity','tranquility','tranquil','silence','silent','atmosphere','calmness','peace','peaceful','pleasant','serene','quiet']

def extract_descriptions(input_list):
    """This function extracts descriptions containing predefined search terms (input_list).
    The descriptions are saved in individual files for each search term (e.g., tranquillity.tsv).
    The function returns two arrays: counts of descriptions per search term and an array of search terms.
    These will be further used to plot the counts distribution."""
    input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input), delimiter='\t', encoding='latin1')
    length = input_text_Geograph.shape[0]
    count_arr = []
    x_labels_arr = []
    for j in input_list:
        print j
        count = 0
        output_file = os.path.join(my_dirpath, 'results/', str(j)+'.tsv')
        output_descriptions = codecs.open(output_file, 'w', 'utf-8')
        output_descriptions.writelines('gridimage_id\tcomment\n')
        for i in range(0, 10000):
            comment = input_text_Geograph["comment"][i]
            try:
                comment = replace_encoding_stuff(str(comment))
                gridimage_id = input_text_Geograph["gridimage_id"][i]
                doc = word_tokenize(str(comment))
                for token in doc:
                    if token.lower() == str(j):
                        count = count + 1
                        output_descriptions.writelines(str(gridimage_id) + '\t' + str(comment) + '\n')
            except:
                print comment
        count_arr.append(count)
        x_labels_arr.append(j)
    n_groups = len(count_arr)
    index = np.arange(n_groups)
    bar_width = 1
    opacity = 0.8
    plt.bar(index, count_arr, bar_width, alpha=opacity, color='#4F97A3', align='center')
    plt.ylabel('Number of descriptions', fontsize=12)
    plt.xticks(index, x_labels_arr, fontsize=12, rotation=70)
    plt.savefig(os.path.join(my_dirpath, 'results.png'), bbox_inches = "tight")
    return

def extract_random(rootdir,sample_size):
    """The function searches for all files in the specified root directory (rootdir).
    The argument 'sample_size' specifies number of random descriptions (e.g., 100) necessary for
    further manual classification."""
    for filename in os.listdir(rootdir):
        doc_id = str(filename[0:-4])
        output_file_random = os.path.join(rootdir, str(doc_id) + '_random.tsv')
        output_descriptions_random = codecs.open(output_file_random, 'w', 'utf-8')
        output_descriptions_random.writelines('gridimage_id\tcomment\n')
        # check that input files are in the same directory or specify below where they are
        input_text = pd.read_csv(os.path.join(rootdir, filename), delimiter='\t', encoding='latin1')
        length = input_text.shape[0]
        dic = {}
        for_random = []
        for i in range(0, length):
            gridimage_id = input_text["gridimage_id"][i]
            comment = input_text["comment"][i]
            dic[gridimage_id] = comment
            for_random.append(gridimage_id)
        if len(for_random) > sample_size:
            selected_random = random.sample(for_random, sample_size)
            for key, value in dic.iteritems():
                if key in selected_random:
                    output_descriptions_random.writelines(str(key) + '\t' + str(value) + '\n')
    return


result = extract_descriptions(search_terms)

random_examples = extract_random(os.path.join(my_dirpath, 'results/'), 2)