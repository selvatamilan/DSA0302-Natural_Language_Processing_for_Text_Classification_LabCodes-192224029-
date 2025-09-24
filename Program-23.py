import spacy
nlp = spacy.load("en_core_web_md")
text = """
Alice went to the park. She saw a dog. It was barking loudly.
Later, she bought ice cream and enjoyed the sunny day.
"""
doc = nlp(text)
sentences = list(doc.sents)
similarities = []
for i in range(len(sentences)-1):
    sim = sentences[i].similarity(sentences[i+1])
    similarities.append(sim)
if similarities:
    coherence_score = sum(similarities)/len(similarities)
else:
    coherence_score = 0.0
print("Consecutive sentence similarities:")
for i, sim in enumerate(similarities):
    print(f"Sentence {i+1} ↔ Sentence {i+2}: {sim:.3f}")

print(f"\nOverall coherence score: {coherence_score:.3f}")
