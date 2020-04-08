
import os
import codecs
import pandas as pd
import random

rootdir = 'C:/Users/ochesnok/Dropbox/tranquillity_LandscapeEcology/100_random_examples'
output_file_random = os.path.join('C:/Users/ochesnok/Dropbox/tranquillity_LandscapeEcology/100_random_examples_2.tsv')
output_descriptions_random = codecs.open(output_file_random, 'w', 'utf-8')
output_descriptions_random.writelines('gridimage_id;;comment\n')

for_random = []
dic = {}
for filename in os.listdir(rootdir):
    print filename
    input_text = pd.read_csv(os.path.join(rootdir, filename), delimiter=';;', encoding='latin1')
    length = input_text.shape[0]

    for i in range(0, length):
        gridimage_id = input_text["gridimage_id"][i]
        comment = input_text["comment"][i]
        dic[gridimage_id] = ((comment,filename[0:-11]))
        for_random.append(gridimage_id)
print len(for_random)
selected_random = random.sample(for_random, 108)
for key, value in dic.iteritems():
    if key in selected_random:
        print key,value
        try:
            output_descriptions_random.writelines(str(key) + ';;' + str(value[0]) + ';;' + str(value[1]) + '\n')
        except:
            continue