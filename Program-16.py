import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is looking at buying U.K. startup for $1 billion. Elon Musk is the CEO of Tesla."

doc = nlp(text)
print("Named Entities, their labels, and positions:")
for ent in doc.ents:
    print(f"{ent.text} → {ent.label_} (start: {ent.start_char}, end: {ent.end_char})")

