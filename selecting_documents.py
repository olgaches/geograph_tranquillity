import os
import codecs
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

dirpath = '//fs.geo.uzh.ch/ochesnok/documents/2_projects/11_tranquillity/corpus/'
filename_input = 'geograph_data/gridimage_text.tsv'

search_terms = ['tranquillity','tranquility','tranquil','silence','silent','atmosphere','calmness','peace','peaceful','pleasant','serene','quiet']

input_text_Geograph = pd.read_csv(os.path.join(dirpath, filename_input), delimiter='\t')
length = input_text_Geograph.shape[0]

def extract_descriptions(input_list):
    for j in input_list:
        print j
        output_file = os.path.join(dirpath, str(j)+'.tsv')
        output_descriptions = codecs.open(output_file, 'w', 'utf-8')
        output_descriptions.writelines('gridimage_id\tcomment\n')
        for i in range(0, 50):
            comment = input_text_Geograph["comment"][i]
            gridimage_id = input_text_Geograph["gridimage_id"][i]
            sentences = sent_tokenize(comment)
            for sentence in sentences:
                sentence_tok = word_tokenize(sentence)
                for word in sentence_tok:
                    if word.lower() == j:
                        output_descriptions.writelines(str(gridimage_id) + '\t' + str(comment) + '\n')

result = extract_descriptions(search_terms)