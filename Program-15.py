import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser
pcfg = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det N [0.6] | N [0.4]
  VP -> V NP [0.7] | V [0.3]
  Det -> 'the' [0.8] | 'a' [0.2]
  N -> 'dog' [0.5] | 'cat' [0.5]
  V -> 'chased' [0.6] | 'saw' [0.4]
""")
parser = ViterbiParser(pcfg)
sentence = "the dog chased a cat".split()
print("Probabilistic Parse Trees:\n")
for tree in parser.parse(sentence):
    print(tree)          
    tree.pretty_print()  
