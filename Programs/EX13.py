import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'dog' | 'cat'
V -> 'chased'
""")

parser = ChartParser(grammar)

sentence = "the dog chased the cat".split()

print("Input Sentence: the dog chased the cat\n")

for tree in parser.parse(sentence):
    print("Generated Parse Tree:\n", tree)
    break
