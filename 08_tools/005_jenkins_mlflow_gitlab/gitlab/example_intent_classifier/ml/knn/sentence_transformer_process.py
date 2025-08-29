from sentence_transformers import SentenceTransformer
from typing import List, Union

# 다국어(한국어 포함) 범용 모델
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def sentence_transformers_processing(texts:Union[List[str], str]):

    if isinstance(texts, List):
        sentences = texts
    else:
        sentences = [texts]
    embeddings = model.encode(sentences, convert_to_numpy=True, normalize_embeddings=True)  # L2 정규화 권장
    return embeddings