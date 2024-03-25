from preprocessings.preprocess import preprocess
from collections import OrderedDict
from positionalIndex.dictionary import Dictionary
from positionalIndex.documents import DocumentList
import math
import time


def query_process(query: str, dictionary: Dictionary, documents: DocumentList, k=10):
    possible_answers = dict()
    preprocessed_query = preprocess(query)
    for word in preprocessed_query:
        if not dictionary.dictionary.__contains__(word):
            continue
        term = dictionary.dictionary[word]
        for docTerm in term.champions_list:
            if term.doc_terms[docTerm].doc_id not in possible_answers:
                possible_answers[term.doc_terms[docTerm].doc_id] = 0
            possible_answers[term.doc_terms[docTerm].doc_id] += term.idf * (1 + math.log(term.doc_terms[docTerm].count))
    for key in possible_answers:
        possible_answers[key] /= dictionary.docs_length[key]
    document_list = []
    for i in range(k):
        if possible_answers.__len__() == 0:
            break
        max_n = 0
        max_k = None
        for key in possible_answers.keys():
            if possible_answers[key] > max_n:
                max_n = possible_answers[key]
                max_k = key
        item = possible_answers.pop(max_k)
        document_list.append(documents.doc_dict[max_k])
    return document_list

