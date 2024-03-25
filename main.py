from positionalIndex import indexing
from queryProcess.queryProcess import query_process
import pickle


def load_indexing():
    try:
        with open('data/dictionary.pkl', 'rb') as file:
            dictionary = pickle.load(file)

        with open('data/documents.pkl', 'rb') as file:
            documents = pickle.load(file)

        return dictionary, documents
    except FileNotFoundError:
        return None, None


dictionary, documents = load_indexing()

if dictionary is None or documents is None:
    dictionary, documents = indexing.index()
else:
    indexing.detect_s_words()


while True:
    query = input('query:')
    documents_list = query_process(query, dictionary, documents)
    with open(f'{query}.text', 'w') as file:
        for document in documents_list:
            print(document, file=file)
