from positionalIndex.term import Term
from typing import List


class Dictionary:
    def __init__(self):
        self.dictionary = dict()
        self.docs_length = dict()
        self.count = 0

    def insert(self, doc: List[str], doc_id: int):
        self.count += doc.__len__()
        for i, word in enumerate(doc):
            if word not in self.dictionary.keys():
                self.dictionary[word] = Term(id(word))
            self.dictionary[word].insert(doc_id, i)

    def calculate_idf(self):
        for key in self.dictionary.keys():
            self.dictionary[key].calculate_idf(self.count)

    def calculate_champions_list(self, r=20):
        for key in self.dictionary.keys():
            self.dictionary[key].calculate_champions_list(r)

    def post_process(self, r=20):
        self.calculate_idf()
        self.calculate_champions_list(r)

    def __str__(self):
        return f"{self.dictionary}"
