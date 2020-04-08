import os
import pandas as pd
import codecs
import nltk
from my_functions import replace_encoding_stuff
from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.parse.stanford import StanfordParser
#
# java_path = 'C:/Program Files (x86)/Java/jre1.8.0_221/bin/java.exe'
# os.environ['JAVAHOME'] = java_path
#
# scp = StanfordParser(path_to_jar='C:/stanford-parser-full-2015-04-20/stanford-parser.jar',
#                      path_to_models_jar='C:/stanford-parser-full-2015-04-20/stanford-parse-models-1.3.2.jar')

import spacy
import numpy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

#
# my_dirpath = '//files.geo.uzh.ch/private/ochesnok/home/Documents/2_projects/11_tranquillity/corpus/'
#
# search_terms_updated = ['tranquillity','tranquility','tranquil','quiet','peaceful','calm']
#
# filename_input_text = 'all_tranquillity_descriptions_coord.csv'
#
# input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input_text), delimiter=';;', encoding='latin1')
# length = input_text_Geograph.shape[0]

# for i in range(0, 1):
#     comment = input_text_Geograph["comment"][i]
#     try:
#         gridimage_id = input_text_Geograph["gridimage_id"][i]
#         comment = replace_encoding_stuff(str(comment))
#         sent_tokenize_list = sent_tokenize(comment)
#         for sentence in sent_tokenize_list:
#
#
#
#
#
#     except:
#         print comment