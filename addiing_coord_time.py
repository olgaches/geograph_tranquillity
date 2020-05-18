#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import codecs
import pandas as pd
from my_functions import replace_encoding_stuff
import nltk
from nltk import word_tokenize
nltk.download('punkt')

my_dirpath = ''
filename_input_text = 'geograph_data/gridimage_text.tsv'
filename_input_base = 'geograph_data/gridimage_base.tsv'

#search_terms = ['tranquillity','tranquility','tranquil','silence','silent','peace','peaceful','serene','quiet','calmness','calm','pleasant','atmosphere']
search_terms_updated = ['tranquillity','tranquility','tranquil','quiet','peaceful','calm']

def extract_descriptions(input_list, output_file):
    """This function extracts descriptions containing predefined search terms (input_list)"""
    input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input_text), delimiter='\t', encoding='latin1')
    length = input_text_Geograph.shape[0]

    input_base_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input_base), delimiter='\t', encoding='latin1')
    length_base = input_base_Geograph.shape[0]

    output_descriptions = codecs.open(output_file, 'w', 'utf-8')
    output_descriptions.writelines('gridimage_id;;user_id;;realname;;title;;image_taken;;x;;y;;wgs84_lat;;wgs84_long;;comment;;search_term;;dependency\n')

    dictionary_text = {}
    for i in range(0, length):
        comment = input_text_Geograph["comment"][i]
        try:
            comment = replace_encoding_stuff(str(comment))
            gridimage_id = input_text_Geograph["gridimage_id"][i]
            doc = word_tokenize(str(comment))
            for token in doc:
                if token.lower() in input_list:
                    dictionary_text[gridimage_id] = [comment,token]

        except:
            print comment

    dictionary_base = {}
    for j in range(0, length_base):
        gridimage_id = input_base_Geograph["gridimage_id"][j]
        user_id = input_base_Geograph["user_id"][j]
        realname = input_base_Geograph["realname"][j]
        title = input_base_Geograph["title"][j]
        image_taken = input_base_Geograph["imagetaken"][j]
        x = input_base_Geograph["x"][j]
        y = input_base_Geograph["y"][j]
        wgs84_lat = input_base_Geograph["wgs84_lat"][j]
        wgs84_long = input_base_Geograph["wgs84_long"][j]
        dictionary_base[gridimage_id] = [user_id,realname,title,image_taken,x,y,wgs84_lat,wgs84_long]

    df1 = pd.DataFrame.from_dict(dictionary_text, "index")
    df1.reset_index(inplace=True)

    df2 = pd.DataFrame.from_dict(dictionary_base, "index")
    df2.reset_index(inplace=True)


    df = df1.merge(df2, left_on="index", right_on="index")
    df.columns = ["gridimage_id", 'comment', 'token', "user_id", "realname", "title", "image_taken", "x", "y", "wgs84_lat", "wgs84_long"]

    for index, row in df.iterrows():
        output_descriptions.writelines(str(row['gridimage_id']) + ';;' + str(row['comment']) + ';;' + str(row['token']) + ';;' + str(row['user_id'])  + ';;' + str(row['realname']) + ';;' + str(row['title']) + ';;' + str(row['image_taken']) + ';;' + str(row['x']) + ';;' + str(row['y']) + ';;' + str(row['wgs84_lat']) + ';;' + str(row['wgs84_long']) + '\n')

    return

result = extract_descriptions(search_terms_updated, os.path.join(my_dirpath, 'all_tranquillity_descriptions_coord.csv'))
