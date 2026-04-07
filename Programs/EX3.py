import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')  
nltk.download('wordnet')

text = "The cats are running and playing happily"

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in tokens]

print("Tokens:", tokens)
print("Lemmatized Words:", lemmas)
