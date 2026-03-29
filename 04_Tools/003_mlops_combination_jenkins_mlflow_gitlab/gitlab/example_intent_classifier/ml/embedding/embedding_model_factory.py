from ml.embedding.sentence_transformer_model import SentenceTransformerModel

# factory pattern
class EmbeddingModelFactory():
    
    def __new__(cls, model_name:str):
        if model_name == 'sentence_transformer':
            return SentenceTransformerModel()
    