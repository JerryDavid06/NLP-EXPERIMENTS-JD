import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.5] | 'John' [0.5]
VP -> V NP [1.0]
Det -> 'the' [1.0]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'chased' [1.0]
""")

parser = ViterbiParser(grammar)

sentence = "the dog chased the cat".split()

print("Input Sentence: the dog chased the cat\n")

for tree in parser.parse(sentence):
    print("Most Probable Parse Tree:\n", tree)
    break
