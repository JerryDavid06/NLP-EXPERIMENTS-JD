import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources (run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = "The dog is running fast"

words = word_tokenize(text)
tags = pos_tag(words)

print(tags)
