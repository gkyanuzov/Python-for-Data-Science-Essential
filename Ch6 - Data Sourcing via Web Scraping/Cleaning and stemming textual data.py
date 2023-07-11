import nltk
from nltk.tokenize import word_tokenize

text = "On Wednesday, the Association for Computing Machinery, the world’s largest society of computing " \
       "professionals, announced that Hinton, LeCun and Bengio had won this year’s Turing Award for their work on " \
       "neural networks. The Turing Award, which was introduced in 1966, is often called the Nobel Prize of " \
       "computing, and it includes a $1 million prize, which the three scientists will share."
word_tk = word_tokenize(text)

# Removing stop words
# nltk.download('stopwords')

from nltk.corpus import stopwords

sw = set(stopwords.words('english'))
print(f"Stop words in english are: {sw}")

filtered_words = [w for w in word_tk if not w in sw]
print(f"The text after removing stop words: {filtered_words}")

# Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

port_stem = PorterStemmer()
stemmed_words = []

for w in filtered_words:
    stemmed_words.append(port_stem.stem(w))

print(f'Filtered Sentence: {filtered_words}')
print(f'Stemmed Sentence: {stemmed_words}')


# Lemmatizing
# nltk.download('wordnet')

from nltk.stem.wordnet import WordNetLemmatizer

lem = WordNetLemmatizer()
stem = PorterStemmer()

lem_words = []

for i in range(len(filtered_words)):
    lem_words.append(lem.lemmatize(filtered_words[i]))

print(f"Lemmatized words: {lem_words}")

# Parts of Speech tagging
# nltk.download('averaged_perceptron_tagger')

from nltk import pos_tag
pos_tagged_word = pos_tag(word_tk)

print(pos_tagged_word)
print('---------------------------------------')
# Frequency distribution plots

from nltk.probability import FreqDist
fd = FreqDist(word_tk)
print(fd)

import  matplotlib.pyplot as plt
fd.plot(30, cumulative=False)
plt.show()