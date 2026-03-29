from ml.embedding.embedding_model import EmbeddingModel
from sentence_transformers import SentenceTransformer
from typing import List, Union

class SentenceTransformerModel(EmbeddingModel):
    
    def __init__(self):
        model = self.init_model()
        self.model = model
    
    def init_model(self):
        sentence_transformer_model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" # 다국어(한국어 포함) 범용 모델
        model = SentenceTransformer(sentence_transformer_model_name)
        return model
    
    def embedding(self, texts:Union[List[str], str]):
        if isinstance(texts, List):
            sentences = texts
        else:
            sentences = [texts]
        embeddings = self.model.encode(sentences, convert_to_numpy=True, normalize_embeddings=True)  # L2 정규화 권장
        return embeddings