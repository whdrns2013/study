
class Vectorizer:
    def fit(self, Documents) -> None:
        raise NotImplementedError
    def transform(self, words_of_doc):
        raise NotImplementedError
    def fit_transform(self, Documents:list[list[str]], words_of_doc:list[str]) -> list[int|float]:
        raise NotImplementedError

class VectorizerContext:
    def __init__(self, vectorizer:Vectorizer):
        self.vectorizer = vectorizer
    def set_vectorizer(self, vectorizer:Vectorizer):
        self.vectorizer = vectorizer
    def fit(self, Documents):
        return self.vectorizer.fit(Documents)
    def transform(self, words_of_doc):
        return self.vectorizer.transform(words_of_doc)
    def fit_transform(self, Documents:list[list[str]], words_of_doc:list[str]) -> list[int|float]:
        return self.vectorizer.fit_transform(Documents, words_of_doc)

# TF-IDF Interface
class TFIDFModel(Vectorizer):
    def tf(self, Documents:list[list[str]]):
        pass
    def idf(self):
        pass
    def tfidf(self):
        raise NotImplementedError
    def fit(self):
        raise NotImplementedError
    def transform(self):
        raise NotImplementedError
    def fit_transform(self):
        raise NotImplementedError

# TF-IDF (전통적 TF-IDF)
class StandardTFIDF(TFIDFModel):
    def __init__(self, Documents:list[list[str]]=None):
        self.Documents:list[list[str]] = Documents
    def tf(self, document:list[str]):
        result = []
        all_word_count = len(document)
        for word in document:
            target_word_count = len([dw for dw in document if dw == word])
            result.append((word, target_word_count/all_word_count))
        return result
    def idf(self, document:list[str]):
        from math import log
        result = []
        document_count = len(self.Documents)
        for word in document:
            include_word_document_count = len([doc for doc in self.Documents if word in doc])
            result.append((word, log(document_count/include_word_document_count)))
        return result
    def tfidf(self, document:list[str]):
        result = []
        for tf, idf in zip(self.tf(document), self.idf(document)):
            result.append((tf[0], tf[1] * idf[1]))
        return result
    def fit(self, Documents:list[list[str]]):
        self.Documents = Documents
        return None
    def transform(self, words_of_doc:list[str]):
        tfidf = self.tfidf(words_of_doc)
        return [x[1] for x in tfidf]
    def fit_transform(self, Documents:list[list[str]], words_of_doc:list[str]) -> list[int|float]:
        self.fit(Documents)
        tfidf = self.transform(words_of_doc)
        return tfidf

# TF-IDF (스무딩 적용)
class SmoothingTFIDF(TFIDFModel):
    def __init__(self, Documents:list[list[str]]=None):
        self.Documents:list[list[str]] = Documents
    def tf(self, document:list[str]):
        result = []
        all_word_count = len(document)
        for word in document:
            target_word_count = len([dw for dw in document if dw == word])
            result.append((word, target_word_count/all_word_count))
        return result
    def idf(self, document:list[str]):
        from math import log
        result = []
        document_count = len(self.Documents) + 1
        for word in document:
            include_word_document_count = len([doc for doc in self.Documents if word in doc]) + 1
            result.append((word, log(document_count/include_word_document_count) + 1))
        return result
    def tfidf(self, document:list[str]):
        result = []
        for tf, idf in zip(self.tf(document), self.idf(document)):
            result.append((tf[0], tf[1] * idf[1]))
        return result
    def fit(self, Documents:list[list[str]]):
        self.Documents = Documents
        return None
    def transform(self, words_of_doc:list[str]):
        tfidf = self.tfidf(words_of_doc)
        return [x[1] for x in tfidf]
    def fit_transform(self, Documents:list[list[str]], words_of_doc:list[str]) -> list[int|float]:
        self.fit(Documents)
        tfidf = self.transform(words_of_doc)
        return tfidf