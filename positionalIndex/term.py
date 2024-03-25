import math


class DocTerm:
    def __init__(self, doc_id: int, term_id: int):
        self.doc_id = doc_id
        self.term_id = term_id
        self.count = 0
        self.positions = []

    def insert(self, position: int):
        self.count += 1
        self.positions.append(position)

    def __str__(self):
        return f"{self.doc_id}: {self.positions}\n"


class Term:
    def __init__(self, term_id: int):
        self.term_id = term_id
        self.count = 0
        self.doc_terms = dict()
        self.champions_list = dict()
        self.idf = 0

    def insert(self, doc_id: int, position: int):
        self.count += 1
        if doc_id not in self.doc_terms.keys():
            self.doc_terms[doc_id] = DocTerm(doc_id, self.term_id)
        self.doc_terms[doc_id].insert(position)

    def calculate_idf(self, n: int):
        self.idf = math.log(n / self.count)

    def calculate_champions_list(self, r=20):
        sorted_doc_terms = sorted(self.doc_terms.items(), key=lambda x: x[1].count, reverse=True)
        top_20_doc_terms = sorted_doc_terms[:r]
        self.champions_list = dict(top_20_doc_terms)

    def __str__(self):
        term_string = f"{self.term_id}:\n"
        for key in self.doc_terms.keys():
            term_string += self.doc_terms[key].__str__()
        return term_string
