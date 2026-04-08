import random

data = [("dog","NN"), ("runs","VB"), ("cat","NN"), ("eats","VB")]

model = {}
for word, tag in data:
    model.setdefault(word, []).append(tag)

def tag(sentence):
    words = sentence.split()
    result = []
    for w in words:
        if w in model:
            result.append((w, random.choice(model[w])))
        else:
            result.append((w, "NN"))
    return result

print(tag("dog eats"))
