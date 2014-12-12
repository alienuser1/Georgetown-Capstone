from __future__ import division
from __future__ import print_function
import nltk, re, pprint, json, os, csv
from nltk import word_tokenize
#
#
# Load the data file into memory
f = open("joe.json")
j_data = json.loads(f.read())
LANGUAGE_SETS = {}
for language in j_data.keys():
LANGUAGE_SETS[language] = set(j_data[language])
f.close()
