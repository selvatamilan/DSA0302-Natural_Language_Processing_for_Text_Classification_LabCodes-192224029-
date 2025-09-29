import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.corpus import wordnet as wn
sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)
np_grammar = r"""
    NP: {<DT>?<JJ>*<NN.*>}   
"""
parser = RegexpParser(np_grammar)
tree = parser.parse(pos_tags)
noun_phrases = []
for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        np_words = [word for word, tag in subtree.leaves()]
        noun_phrases.append(" ".join(np_words))
print("\nNoun Phrases:", noun_phrases)
print("\nNoun Phrase Meanings:")
for np in noun_phrases:
    head_word = np.split()[-1]
    synsets = wn.synsets(head_word)
    if synsets:
        print(f"{np}:")
        for syn in synsets[:2]:  
            print(f"  - {syn.definition()}")
    else:
        print(f"{np}: No meaning found in WordNet.")

