from pythainlp.tokenize import word_tokenize
from pythainlp.tag import pos_tag, NER

def tokenize_text(text):
    return word_tokenize(text, engine='newmm')

def pos_tag_text(tokens):
    return pos_tag(tokens, engine='perceptron')

def ner_tag_text(text):
    ner = NER("thainer")
    return ner.tag(text)
