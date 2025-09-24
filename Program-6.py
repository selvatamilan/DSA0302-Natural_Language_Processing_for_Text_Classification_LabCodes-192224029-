import random
import nltk
from nltk.tokenize import word_tokenize
text = """Natural language processing (NLP) is a field of artificial intelligence.
It focuses on the interaction between computers and humans through language.
NLP is widely used in applications such as chatbots, machine translation, and text summarization."""

tokens = word_tokenize(text)

bigrams = {}
for i in range(len(tokens) - 1):
    curr_word = tokens[i]
    next_word = tokens[i + 1]
    if curr_word not in bigrams:
        bigrams[curr_word] = []
    bigrams[curr_word].append(next_word)

def generate_text(start_word, num_words=15):
    word = start_word
    result = [word]
    
    for _ in range(num_words - 1):
        if word in bigrams:
            word = random.choice(bigrams[word])  
        else:
            break
        result.append(word)
    
    return " ".join(result)

print("Generated Text:")
print(generate_text("NLP", 20))
