import csv
import json
from json import encoder
import re
from pprint import pprint
list_dict = []

old_data_lines =  open('jpn_eng_sentences.tsv', encoding='utf8').read().split('\n')

for line in old_data_lines:
    parsed_line = line.split('\t')
    list_dict.append({"jpn": parsed_line[1] , "en":parsed_line[3]})

with open('parsed_data.txt', 'w', encoding='utf8') as outfile:
    foo = json.dumps(list_dict, ensure_ascii=False).encode('utf8')
    outfile.write(foo.decode())



