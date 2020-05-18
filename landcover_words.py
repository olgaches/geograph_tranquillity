#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import pandas as pd
from collections import Counter
import math
import codecs

my_dirpath = ''
landcover_class = 'arable'
filename_input_text = landcover_class + '.csv'

output_file_all = os.path.join(my_dirpath, landcover_class + '_all.csv')
output_descriptions_all = codecs.open(output_file_all, 'w', 'utf-8')

output_file_winter = os.path.join(my_dirpath, landcover_class + '_winter.csv')
output_descriptions_winter = codecs.open(output_file_winter, 'w', 'utf-8')

output_file_spring = os.path.join(my_dirpath, landcover_class + '_spring.csv')
output_descriptions_spring = codecs.open(output_file_spring, 'w', 'utf-8')

output_file_summer = os.path.join(my_dirpath, landcover_class + '_summer.csv')
output_descriptions_summer = codecs.open(output_file_summer, 'w', 'utf-8')

output_file_autumn = os.path.join(my_dirpath, landcover_class + '_autumn.csv')
output_descriptions_autumn = codecs.open(output_file_autumn, 'w', 'utf-8')

input_text_Geograph = pd.read_csv(os.path.join(my_dirpath, filename_input_text), delimiter=';;', encoding='latin1')
length = input_text_Geograph.shape[0]

words_winter = []
words_spring = []
words_summer = []
words_autumn = []
all_words = []
for i in range(0, length):
    gridimage_id = input_text_Geograph["gridimage_id"][i]
    dependency_word = input_text_Geograph["dependency"][i].lower()
    month = input_text_Geograph["month"][i]
    all_words.append(dependency_word)
    if month == 12 or month == 1 or month == 2:
        words_winter.append(dependency_word)
    elif month == 3 or month == 4 or month == 5:
        words_spring.append(dependency_word)
    elif month == 6 or month == 7 or month == 8:
        words_summer.append(dependency_word)
    elif month == 11 or month == 10 or month == 9:
        words_autumn.append(dependency_word)

result_all = sorted(Counter(all_words).items(), key=lambda pair: pair[1], reverse=True)
result_winter = sorted(Counter(words_winter).items(), key=lambda pair: pair[1], reverse=True)
result_spring = sorted(Counter(words_spring).items(), key=lambda pair: pair[1], reverse=True)
result_summer = sorted(Counter(words_summer).items(), key=lambda pair: pair[1], reverse=True)
result_autumn = sorted(Counter(words_autumn).items(), key=lambda pair: pair[1], reverse=True)

print result_all
print result_winter
print result_spring
print result_summer
print result_autumn


for key, value in result_all:
    output_descriptions_all.writelines(str(key) + ':' + str(math.log(value)) + '\n')

for key, value in result_winter:
    output_descriptions_winter.writelines(str(key) + ':' + str(math.log(value)) + '\n')

for key, value in result_spring:
    output_descriptions_spring.writelines(str(key) + ':' + str(math.log(value)) + '\n')

for key, value in result_summer:
    output_descriptions_summer.writelines(str(key) + ':' + str(math.log(value)) + '\n')

for key, value in result_autumn:
    output_descriptions_autumn.writelines(str(key) + ':' + str(math.log(value)) + '\n')