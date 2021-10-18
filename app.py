import csv
import json
from json import encoder
import re
from pprint import pprint
jap_eng_list = []

TSV_FILE = 'jpn_eng_sentences.tsv'


def parse_tsv(TSV_FILE)
	"""
	Parse a .tsv file and create a list of dictionary entries that have the 
	japanese and english meanings
		
	"""
	tsv_data =  open(TSV_FILE, encoding='utf8').read().split('\n')

	for line in tsv_data:
	    parsed_line = line.split('\t')
	    jap_eng_list.append({"jpn": parsed_line[1] , "en":parsed_line[3]})

	create_json_file(jap_eng_list)


def create_json_file(list_dict, json_func=json)
	"""
	Create a json file from the list of dictionary objects

	Example:
		input:
			[
				{'jap': 'japanese_word', 'eng': 'english_word'}
			]
		output: jap_eng_list.json
	"""
	with open('jap_eng_list.json', 'w', encoding='utf8') as outfile:
	    foo = json_func.dumps(list_dict, ensure_ascii=False).encode('utf8')
	    outfile.write(foo.decode())


def main():
	# parse data from the file given
	parse_tsv(TSV_FILE)


if __name__ == '__main__':
	main()


