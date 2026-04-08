# Initial tagging
sentence = "dog runs fast"
words = sentence.split()
tags = ["NN"] * len(words)

# Transformation rule
for i in range(len(words)):
    if words[i].endswith("s"):
        tags[i] = "VB"

print(list(zip(words, tags)))
