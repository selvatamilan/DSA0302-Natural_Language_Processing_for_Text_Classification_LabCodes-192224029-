import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger
patterns = [
    (r'.*ing$', 'VBG'),      
    (r'.*ed$', 'VBD'),       
    (r'.*es$', 'VBZ'),       
    (r'.*s$', 'NNS'),        
    (r'^-?[0-9]+$', 'CD'),   
    (r'.*ly$', 'RB'),        
    (r'.*able$', 'JJ'),      
    (r'.*ness$', 'NN'),      
    (r'.*ment$', 'NN'),      
    (r'.*ful$', 'JJ'),       
    (r'.*', 'NN')            
]
regex_tagger = RegexpTagger(patterns)
text = "The quick brown fox is jumping over the lazy dogs happily"
tokens = word_tokenize(text)
tagged_tokens = regex_tagger.tag(tokens)

print("Rule-Based POS Tagging Results:")
for word, tag in tagged_tokens:
    print(f"{word} → {tag}")
