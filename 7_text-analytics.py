'''7) Text Analytics
1. Extract Sample document and apply following document preprocessing methods:
Tokenization, POS Tagging, stop words removal, Stemming and Lemmatization.
2. Create representation of documents by calculating Term Frequency and Inverse
DocumentFrequency.'''


import nltk
nltk.download('all')

# Tokenization using NLTK
from nltk import word_tokenize, sent_tokenize
sent = "The sun shines brightly in the clear blue sky.Birds chirp melodiously as they flit from tree to tree.The scent of freshly baked bread wafts through the air.Children laugh and play in the green meadow, chasing butterflies.A gentle breeze rustles the leaves, creating a soothing symphony of nature."
print(word_tokenize(sent))
print(sent_tokenize(sent))

from nltk.stem import PorterStemmer

# create an object of class PorterStemmer
porter = PorterStemmer()
print(porter.stem("play"))
print(porter.stem("playing"))
print(porter.stem("plays"))
print(porter.stem("played"))

print(porter.stem("Communication"))

from nltk.stem import WordNetLemmatizer
# create an object of class WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("plays", 'v'))
print(lemmatizer.lemmatize("played", 'v'))
print(lemmatizer.lemmatize("play", 'v'))
print(lemmatizer.lemmatize("playing", 'v'))

print(lemmatizer.lemmatize("Communication", 'v'))

from nltk import pos_tag
from nltk import word_tokenize

text = "The sun shines brightly in the clear blue sky"
tokenized_text = word_tokenize(text)
tags = tokens_tag = pos_tag(tokenized_text)
tags

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
text = "This is an example sentence demonstrating stop word removal."
filtered_text = [word for word in word_tokenize(text) if word.lower() not in stop_words]
print(filtered_text)

import re

text = "This is a sentence with, punctuation!"
clean_text = re.sub(r'[^\w\s]', '', text)
print(clean_text)

part 2

from sklearn.feature_extraction.text import TfidfVectorizer

# creation of documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the documents to calculate TF-IDF representation
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Convert TF-IDF matrix to array for easier manipulation
tfidf_array = tfidf_matrix.toarray()

# Get feature names (terms)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Print TF-IDF matrix (document-term matrix)
print("TF-IDF Matrix (Document-Term Matrix):")
print(tfidf_array)

# Print feature names (terms)
print("\nFeature Names (Terms):")
print(feature_names)

