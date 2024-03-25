class Document:
    def __init__(self, title: str, content: str, category: str, url: str):
        self.title = title
        self.content = content
        self.category = category
        self.url = url

    def __str__(self):
        document_string = self.title + self.content + self.category + '\n' + self.url
        document_string += '\n------------------------------------------'
        return document_string


class DocumentList:
    def __init__(self):
        self.doc_dict = dict()

    def insert(self,doc_id: int, title: str, content: str, category: str, url: str):
        self.doc_dict[doc_id] = Document(title, content, category, url)



