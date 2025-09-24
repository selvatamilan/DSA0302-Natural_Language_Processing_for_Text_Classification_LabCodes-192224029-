import spacy
nlp = spacy.load("en_core_web_sm")
text = "Alice went to the park. She saw a dog. It was barking loudly."
doc = nlp(text)
pronoun_map = {}
for token in doc:
    if token.pos_ == "PRON" and token.dep_ in ("nsubj", "dobj"):
        for prev_token in reversed(list(doc[:token.i])):
            if prev_token.pos_ in ("PROPN", "NOUN"):
                pronoun_map[token.text] = prev_token.text
                break
print("Pronoun resolutions:")
for pronoun, ref in pronoun_map.items():
    print(f"{pronoun} -> {ref}")
