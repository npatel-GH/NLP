# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 00:43:49 2019

@author: Welcome
"""

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

sentence = "This is exercise that helps to understand what we have learnt"

stopwords = set(stopwords.words('english')) 

wordtokens = word_tokenize(sentence) 

filtered = [w for w in wordtokens if not w in stopwords] 

filtered = [] 

for w in wordtokens: 
	if w not in stopwords: 
		filtered.append(w) 

print(wordtokens) 
print(filtered) 
