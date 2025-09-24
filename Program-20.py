from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "Natural language processing is a field of artificial intelligence.",
    "Machine learning and deep learning are popular AI techniques.",
    "Information retrieval uses algorithms to rank documents based on relevance.",
    "TF-IDF is commonly used in information retrieval systems.",
    "Python is a popular programming language for NLP and AI."
]
query = "AI and natural language processing"
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])
similarity_scores = cosine_similarity(query_vector, doc_vectors).flatten()
ranked_indices = similarity_scores.argsort()[::-1]  
print("Documents ranked by relevance to the query:\n")
for idx in ranked_indices:
    print(f"Score: {similarity_scores[idx]:.4f} -> Document: {documents[idx]}")
