import nltk

#Using NLTKs own data
from nltk.corpus import reuters
words = reuters.words()

#Word counts
from nltk import FreqDist
FreqDist(words)
FreqDist(words).most_common(50)

#Stopwords
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

#Obtain vocabulary from text
#We want to focus on first headline
sentences = reuters.sents()
vocabulary = set(sentences[0])

#Loop to remove
clean_text = []
for word in vocabulary:
	if word in stop:
		clean_text.append(word)

#clean the text even more by applying lowercase

#POS tagging
nltk.pos_tag(sentences)
nltk.help.upenn_tagset('JJ')
nltk.help.upenn_tagset('IN')
nltk.help.upenn_tagset('NNP')

#bigrams
from nltk import bigrams as b
bigrams = b(sentences[0])

#trigrams
from nltk import trigrams as t
trigrams = t(sentences[0])

#Use the vocabulary above to generte the bag of words representation
vocabulary = list(vocabulary)
#Generate the bag of words representation

#Using NLTK to train a Naive Bayes classifier
from nltk.corpus import names
labeled_names = []

for name in names.words('male.txt'):
	labeled_names.append((name, 'male'))

for name in names.words('female.txt'):
	labeled_names.append((name, 'female'))

import random
random.shuffle(labeled_names)

featuresets = []
for n in labeled_names:
	features = {}
	last_letter = n[0][-1]
	features['last_letter'] = last_letter
	featuresets.append((features, n[1]))

train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

#Naive Bayes classifier
from nltk.corpus import movie_reviews

files = list(movie_reviews.fileids())
documents = []

for f in files:
	documents.append((list(movie_reviews.words(f)), movie_reviews.categories(f)[0]))

random.shuffle(documents)

#Obtain features
all_words = []
for word in movie_reviews.words():
	all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words)[:2000]

#Create featureset for all documents
featureset = []
for doc in documents:
	features = {}
	for word in word_features:
		if word in doc[0]:
			features[word] = True
		else:
			features[word] = False

	featureset.append((features, doc[1]))

train_set, test_set = featureset[100:], featureset[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
