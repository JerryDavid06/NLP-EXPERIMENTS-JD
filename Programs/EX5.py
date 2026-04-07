from nltk.stem import PorterStemmer

words = ["running", "played", "happiness", "studies"]

ps = PorterStemmer()

for word in words:
    print(word, "->", ps.stem(word))
