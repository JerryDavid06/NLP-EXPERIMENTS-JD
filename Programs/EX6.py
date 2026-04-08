import random

text = "I love NLP and I love Python"
words = text.split()

# Create bigrams
bigrams = {}
for i in range(len(words)-1):
    key = words[i]
    value = words[i+1]
    bigrams.setdefault(key, []).append(value)

# Generate text
word = random.choice(words)
result = [word]

for _ in range(5):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)

print("Generated Text:", " ".join(result))
