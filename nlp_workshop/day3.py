import nltk
import json

#Import text to analyze
from nltk.corpus import reuters

#Use sentences
sentences = list(reuters.sents())

#Do some data pre-processing
def lowercase(word):
	return word.lower()

def processSentences(sent):
	return map(lowercase, sent)

sentences = map(processSentences, sentences)

#Sentiment Analysis
#Method 1. Dictionaries

affin = open('AFINN_english.txt')
sentimentScores = {}

for line in affin:
	term, score = line.split("\t")
	sentimentScores[term] = float(score)

#Proceed with sentiment analysis
newsSentiment = []

for sent in sentences:
	score = 0
	for word in sent:
		try:
			score += sentimentScores[word]
		except:
			pass
	if score > 0:
		sentiment = 'positive'
	elif score < 0:
		sentiment = 'negative'
	else:
		sentiment = 'neutral'
	s = ' '.join(sent)
	newsSentiment.append((s, sentiment))

#Doing the same sentiment analysis task
import random
random.shuffle(newsSentiment)

all_words = reuters.words()

#Use previously defined function
all_words = map(lowercase, all_words)

#Pre-process data
from nltk.corpus import stop
stop = set(stop.words("english"))

all_words_clean = []
for word in all_words:
	if (word not in stop) and (len(word) > 2):
		all_words_clean.append(word)

all_words_clean = nltk.FreqDist(all_words_clean)

word_features = list(all_words_clean)[:2000]
#Not clean
#word_features = list(all_words)[:2000]

#Create featureset for all documents
featureset = []
for doc in newsSentiment:
	features = {}
	for word in word_features:
		if word in doc[0]:
			features[word] = True
		else:
			features[word] = False
	featureset.append((features, doc[1]))

#Entity recognition
#Go to http://nlp.stanford.edu/software/stanford-ner-2014-08-27.zip and download Stanford NER
#Locate it in a place where you will find it
from nltk.tag import StanfordNERTagger
english_tagger = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz','stanford-ner.jar')
english_tagger.tag("Mark is gettin impatient about the results KPMG might report.".split())
