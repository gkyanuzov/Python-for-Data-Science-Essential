# stemming - sitting --> sit; run, ran, running ---> root word: run;
# lemmatizing - raw text:better, base word: good

import nltk

text = "On Wednesday, the Association for Computing Machinery, the world’s largest society of computing " \
       "professionals, announced that Hinton, LeCun and Bengio had won this year’s Turing Award for their work on " \
       "neural networks. The Turing Award, which was introduced in 1966, is often called the Nobel Prize of " \
       "computing, and it includes a $1 million prize, which the three scientists will share."

# nltk.download('punkt')

# Sentence tokenizer
from nltk.tokenize import sent_tokenize

sent_tk = sent_tokenize(text)
print(f"Sentence tokenizing the text: {sent_tk}")

# Word tokenizer
from nltk.tokenize import word_tokenize

word_tk = word_tokenize(text)
print(f"Word tokenizing the text: {word_tk}")

