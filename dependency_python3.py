import pandas as pd
import os
import codecs
import spacy
from collections import Counter

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")

my_dirpath = ''

output_file = os.path.join(my_dirpath, 'all_tranquillity_dependencies_dates.csv')
output_descriptions = codecs.open(output_file, 'w', 'utf-8')
output_descriptions.writelines('gridimage_id;;comment;;serach_term;;dependency_word;;date;;year;;month;;\n')

search_terms_updated = ['tranquillity','tranquility','tranquil','quiet','peaceful','calm']

filename_input_text = 'all_tranquillity_descriptions_coord.csv'

input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input_text), delimiter=';;', encoding='latin1')
length = input_text_Geograph.shape[0]

dependency_words = []
for i in range(0, length): 
    comment = input_text_Geograph["comment"][i]
    try:
        gridimage_id = input_text_Geograph["gridimage_id"][i]
        date = input_text_Geograph["image_taken"][i]
        year = date[0:4]
        month = date[5:7]
        doc = nlp(comment)
        for token in doc:
            if token.dep_ == 'amod' and token.text in search_terms_updated:
                #print(token.text, token.dep_, token.head.text)
                #print(gridimage_id,token.text,token.head.text)
                dependency_words.append(token.head.text)
                output_descriptions.writelines(str(gridimage_id)+';;'+str(comment)+';;'+str(token.text)+';;'+str(token.head.text)+';;'+str(date)+';;'+str(year)+';;'+str(month)+'\n')
    except:
        print(comment)
        
set_result = ([[l, dependency_words.count(l)] for l in set(dependency_words)])

print(sorted(set_result, key=lambda set_result: set_result[1], reverse = True)) 
