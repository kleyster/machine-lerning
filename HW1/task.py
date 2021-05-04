import re
import numpy as np
import pandas

sentences = []

with open('sentences.txt','r') as file:
	for i in file:
		sentences.append(i.lower().strip())

for i in range(len(sentences)):
	sentences[i] = re.split(r'[^a-z]',sentences[i])
	while sentences[i].count("") > 0:
		sentences[i].remove("")


words = []
word=[]
for i in sentences:
	for j in i:
		word.append(j)
		if j not in words:
			words.append(j)

dictionary = {}

for i in range(len(words)):
	dictionary[words[i]] = i


mtrx = np.zeros((len(sentences),len(dictionary)))

for i,j in enumerate(sentences):
	for z in dictionary:
		mtrx[i][dictionary[z]] = j.count(z)


def cos_d(x,y):
	return 1-x@y/(np.sqrt(x@x)*np.sqrt(y@y))

mtrx.shape
d = np.array([cos_d(mtrx[0],mtrx[i]) for i in range(1,mtrx.shape[0])])

w()