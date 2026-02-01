# utils.py
# Helper functions for text processing

import string

def preprocess_text(text):
    
    text = text.lower()

    text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))

    text = " ".join(text.split())

    return text
