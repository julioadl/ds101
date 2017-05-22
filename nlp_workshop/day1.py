import nltk

#Download NLTK dependencies
nltk.download()

#Testing NLTK is working using the brown corpus
from nltk.corpus import brown
brown.words([0:10])
brown.tagged_words()[0:10]
len(brown.words())
dir(brown)

#Test NLTK book resources
from nltk.book import *
dir(text1)
len(text1)

#Tokenization
from nltk import word_tokenize, sent_tokenize
text = "Imperial College London is a public research university located in London, United Kingdom. Its founder, Prince Albert, envisioned an area comprising the Victoria and Albert Museum, Natural History Museum, Royal Albert Hall, and the Imperial Institute. His wife, Queen Victoria, laid the foundation stone for the Imperial Institute in 1888. Imperial College London was granted Royal Charter in 1907. In the same year, the college joined the University of London, before leaving it a century later.[9] Through merging with several historic medical schools, the curriculum expanded to include medicine. In 2004, Queen Elizabeth II opened the Imperial College Business School."

sentences = sent_tokenize(text)
sentences
len(sentences)
tokens = word_tokenize(sentences)
tokens

#More on NLTK tokenizers
#English tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#Spanish tokenizer
spanish_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
texto = "Un buen reportaje puede ser tan fascinante e instructivo sobre el mundo real como un gran cuento o una magnífica novela. Si alguien lo pone en duda, le ruego que lea la crónica de Ioan Grillo Bring On the Wall que apareció en The New York Times el pasado 7 de mayo. Cuenta la historia del Flaco, un contrabandista mexicano que, desde que estaba en el colegio, a los 15 años, se ha pasado la vida contrabandeando drogas e inmigrantes ilegales a Estados Unidos. Aunque estuvo cinco años en la cárcel no se ha arrepentido del oficio que practica y menos ahora, cuando, dice, su ilícita profesión está más floreciente que nunca."
spanish_tokenizer.tokenize(texto)

#Different types of tokenizers (and how to call different methods on NLTK)
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokenizer.tokenize("This's a test")

from nltk.tokenize import PunktWordTokenizer
punkt_word_tokenizer = PunktWordTokenizer()
punkt_word_tokenizer.tokenize("this's a test")

from nltk.tokenize import WordPunctTokenizer
word_punct_tokenizer = WordPunctTokenizer()
word_punct_tokenizer.tokenize("this's a test")

#Stemming
#Using the porter algorithm
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem('maximum')
porter_stemmer.stem('presumably')
porter_stemmer.stem('multiply')
porter_stemmer.stem('provision')
porter_stemmer.stem('owed')
porter_stemmer.stem('ear')
porter_stemmer.stem('saying')

#Using the Lancaster algorithm
from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
lancaster_stemmer.stem('maximum')
lancaster_stemmer.stem('presumably')
lancaster_stemmer.stem('multiply')
lancaster_stemmer.stem('provision')
lancaster_stemmer.stem('owed')
lancaster_stemmer.stem('ear')
lancaster_stemmer.stem('saying')

#Snowball stemmer
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer(“english”)
snowball_stemmer.stem('maximum')
snowball_stemmer.stem('presumably')
snowball_stemmer.stem('multiply')
snowball_stemmer.stem('provision')
snowball_stemmer.stem('owed')
snowball_stemmer.stem('ear')
snowball_stemmer.stem('saying')

#Lemmatization
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
wordnet_lemmatizer.lemmatize('dogs')
wordnet_lemmatizer.lemmatize('churches')
wordnet_lemmatizer.lemmatize('aardwolves')
wordnet_lemmatizer.lemmatize('abaci')
wordnet_lemmatizer.lemmatize('hardrock')
wordnet_lemmatizer.lemmatize('are')
wordnet_lemmatizer.lemmatize('is')

#lemmatizer default is 'n', hence one has to change to 'v'
wordnet_lemmatizer.lemmatize('is', pos='v')
wordnet_lemmatizer.lemmatize('is', pos='v')

#POS tagging
nltk.pos_tag(text)
nltk.help.upenn_tagset('JJ')
nltk.help.upenn_tagset('IN')
nltk.help.upenn_tagset('NNP')

#Stopwords
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
#Loop to remove

#Word counts
from nltk import FreqDist
FreqDist(text)
FreqDist(text.split())
FreqDist(text.split()).most_common(50)