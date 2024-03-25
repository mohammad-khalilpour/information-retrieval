import json
import pickle
from preprocessings.preprocess import preprocess, detect_stop_words
from positionalIndex.dictionary import Dictionary
from positionalIndex.documents import DocumentList


def read_json(path):
    file = open(path)
    data = json.load(file)
    return data


def index(path='data/IR_data_news_12k.json'):
    dictionary = Dictionary()
    documents = DocumentList()

    data = read_json(path)

    all_content = ''
    for i in data:
        all_content += data[i]['content']

    detect_stop_words(all_content)

    for i in data:

        content = data[i]['content']

        documents.insert(i, data[i]['title'], data[i]['content'], data[i]['category'], data[i]['url'])
        preprocessed_content = preprocess(content)
        dictionary.docs_length[i] = preprocessed_content.__len__()
        dictionary.insert(preprocessed_content, i)

    dictionary.post_process()

    with open('data/dictionary.pkl', 'wb') as file:
        pickle.dump(dictionary, file)

    with open('data/documents.pkl', 'wb') as file:
        pickle.dump(documents, file)

    return dictionary, documents


def detect_s_words(path='data/IR_data_news_12k.json'):

    data = read_json(path)

    all_content = ''
    for i in data:
        all_content += data[i]['content']

    detect_stop_words(all_content)
