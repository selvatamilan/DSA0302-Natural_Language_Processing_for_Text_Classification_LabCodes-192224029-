import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
sentence = "I went to the bank to deposit some money."
tokens = word_tokenize(sentence)
target_word = "bank"
sense = lesk(tokens, target_word)
if sense:
    print(f"Target word: {target_word}")
    print(f"Sense chosen by Lesk: {sense.name()}")
    print(f"Definition: {sense.definition()}")
    print(f"Examples: {sense.examples()}")
else:
    print(f"No sense found for '{target_word}'")
