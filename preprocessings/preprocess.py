from preprocessings.tokenizer.tokenizer import Tokenizer
from preprocessings.normalizer.normalizer import Normalizer
from hazm import lemmatizer

tokenizer = Tokenizer()
normalizer = Normalizer()
stemmer = lemmatizer.Lemmatizer()


def detect_stop_words(content):
    normalizer.detect_stop_words(content)


def preprocess(content):
    tokenized_content = tokenizer.tokenize(content)
    normalized_content = normalizer.normalize(tokenized_content)
    for j in range(normalized_content.__len__()):
        normalized_content[j] = stemmer.lemmatize(normalized_content[j])
    return normalized_content
