import re

def tag(word):
    if re.match(r'.*ing$', word):
        return "VBG"
    elif re.match(r'.*ed$', word):
        return "VBD"
    elif re.match(r'.*s$', word):
        return "NNS"
    else:
        return "NN"

sentence = "dogs are running"
words = sentence.split()

print([(w, tag(w)) for w in words])
