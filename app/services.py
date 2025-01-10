import pandas as pd
import os
import sys
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nlp = spacy.load("en_core_web_sm")

# File finder
def find_file_path(file):
    file_path = None
    sys.path.insert(0, "/home/john/Documents/fastapi/chats_with_intents/")
    for path in sys.path:
        pot_path = os.path.join(path, file)
        if os.path.exists(pot_path):
            file_path = pot_path
            break
    return file_path if file_path else "No path for such file"

# Data extractor
def data_extraction():
    file_path = find_file_path("dataSet.xlsx")
    df = pd.read_excel(file_path)
    return df

# Preprocessing function
def preprocessing(sentences):
    preprocessed_sentences = []
    for sent in sentences:
        doc = nlp(sent)
        tokens = []
        for token in doc:
            if not token.is_stop and not token.is_punct:
                tokens.append(token.lemma_)
        preprocessed_sentences.append(" ".join(tokens))
    return preprocessed_sentences

# Vectorization
def vectorization(sentences, vectorizer=None):
    if vectorizer is None:
        vectorizer = CountVectorizer()
        x = vectorizer.fit_transform(sentences)
        return x, vectorizer
    else:
        x = vectorizer.transform(sentences)
        return x

# Training function
def training():
    data = data_extraction()
    intents = data["Intent"].tolist()
    sentences = data["Sentence"].tolist()
    preprocessed_sentences = preprocessing(sentences)
    x, vectorizer = vectorization(preprocessed_sentences)
    classifier = LogisticRegression()
    classifier.fit(x, intents)
    return classifier, vectorizer

# Main code
classifier, vectorizer = training()

# Test phase
test_sentence = "How's the day?"
test_processed = preprocessing([test_sentence])  # Wrap test sentence in a list
test_vector = vectorization(test_processed, vectorizer)
predicted_intent = classifier.predict(test_vector)

print(f"Sentence: {test_sentence}")
print(f"Predicted Intent: {predicted_intent[0]}")
