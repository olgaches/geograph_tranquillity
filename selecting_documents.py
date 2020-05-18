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

my_dirpath = ''
filename_input = 'geograph_data/gridimage_text.tsv'

search_terms = ['tranquillity','tranquility','tranquil','silence','silent','peace','peaceful','serene','quiet','calmness','calm','pleasant','atmosphere']
search_terms_updated = ['tranquillity','tranquility','tranquil','quiet','peaceful','calm']

def extract_descriptions(input_list, output_file):
    """This function extracts descriptions containing predefined search terms (input_list)"""
    input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input), delimiter='\t', encoding='latin1')
    length = input_text_Geograph.shape[0]
    output_descriptions = codecs.open(output_file, 'w', 'utf-8')
    output_descriptions.writelines('gridimage_id;;comment;;search_term\n')
    for i in range(0, length):
        comment = input_text_Geograph["comment"][i]
        try:
            comment = replace_encoding_stuff(str(comment))
            gridimage_id = input_text_Geograph["gridimage_id"][i]
            doc = word_tokenize(str(comment))
            for token in doc:
                if token.lower() in input_list:
                    output_descriptions.writelines(str(gridimage_id) + ';;' + str(comment) + ';;' + str(token) + '\n')
        except:
            print comment
    return


def extract_individual_descriptions(input_file):
    """This function creates individual files for each search term (e.g., tranquillity.tsv)
    and plots how many of them are present in the descriptions"""
    input_text_tranquillity = pd.read_csv(os.path.join(my_dirpath, input_file), delimiter=';;', encoding='latin1')
    length = input_text_tranquillity.shape[0]

    terms_dic = {}
    for i in range(0, length):
        comment = input_text_tranquillity["comment"][i]
        gridimage_id = input_text_tranquillity["gridimage_id"][i]
        search_term = input_text_tranquillity["search_term"][i]
        if search_term.lower() in terms_dic.keys():
            terms_dic[search_term.lower()].append((gridimage_id, comment))
        else:
            terms_dic[search_term.lower()] = [(gridimage_id, comment)]
    unique_keys = set(terms_dic.keys())
    for j in unique_keys:
        print j
        output_file = os.path.join(my_dirpath, 'results/', str(j)+'.tsv')
        output_descriptions = codecs.open(output_file, 'w', 'utf-8')
        output_descriptions.writelines('gridimage_id;;comment\n')
        individual_descriptions = terms_dic.get(j)
        for i in individual_descriptions:
            try:
                output_descriptions.writelines(str(i[0]) + ';;' + str(i[1]) + '\n')
            except:
                print 'to fix',i
    count_arr = []
    x_labels_arr = []
    for k, v in terms_dic.iteritems():
        count_arr.append(len(v))
        x_labels_arr.append(k)
    n_groups = len(count_arr)
    index = np.arange(n_groups)
    bar_width = 1
    opacity = 0.8
    plt.bar(index, count_arr, bar_width, alpha=opacity, color='#4F97A3', align='center')
    plt.ylabel('Number of descriptions', fontsize=12)
    plt.xticks(index, x_labels_arr, fontsize=12, rotation=70)
    plt.savefig(os.path.join(my_dirpath, 'results.png'), bbox_inches = "tight")
    return

def extract_random(rootdir, sample_size):
    """The function searches for all files in the specified root directory (rootdir).
    The argument 'sample_size' specifies number of random descriptions (e.g., 100) necessary for
    further manual classification."""
    for filename in os.listdir(rootdir):
        print filename
        doc_id = str(filename[0:-4])
        output_file_random = os.path.join(rootdir, str(doc_id) + '_random.tsv')
        output_descriptions_random = codecs.open(output_file_random, 'w', 'utf-8')
        output_descriptions_random.writelines('gridimage_id;;comment\n')
        # check that input files are in the same directory or specify below where they are
        input_text = pd.read_csv(os.path.join(rootdir, filename), delimiter=';;', encoding='latin1')
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
                    output_descriptions_random.writelines(str(key) + ';;' + str(value) + '\n')
    return

results_file = os.path.join(my_dirpath, 'all_tranquillity_descriptions.tsv')

#result = extract_descriptions(search_terms, results_file)
#print 'the big tranquillity file is here'

#individual_files = extract_individual_descriptions(results_file)
#print 'the individual files are created'

random_examples = extract_random(os.path.join(my_dirpath, 'results/'), 100)
