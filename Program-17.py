import nltk
from nltk.corpus import wordnet as wn
word = "bank"
synsets = wn.synsets(word)
print(f"Synsets of '{word}':\n")
for i, syn in enumerate(synsets, start=1):
    print(f"{i}. {syn.name()} - {syn.definition()}")
    print(f"   Examples: {syn.examples()}")
print("\n")
if synsets:
    syn = synsets[0]  
    print(f"Exploring relationships for synset: {syn.name()}\n")
    hypernyms = syn.hypernyms()
    print("Hypernyms:", [h.name() for h in hypernyms])
    hyponyms = syn.hyponyms()
    print("Hyponyms:", [h.name() for h in hyponyms])
    lemmas = syn.lemmas()
    print("Lemmas:", [l.name() for l in lemmas])
