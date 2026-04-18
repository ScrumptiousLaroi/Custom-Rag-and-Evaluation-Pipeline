from sentence_transformers import SentenceTransformer
import numpy as np

def get_embedding_model(model_name: str= "all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)

def embed_chunks(chunks: list[dict], model) -> tuple[list[str], np.ndarray]:
    chunk_texts = [c.get("chunk_text", "") for c in chunks if c.get("chunk_text", "").strip()]
    embeddings = model.encode(chunk_texts, normalize_embeddings=True) #Normalize is important for cosine simalrity and retrieval code gets easier and faster

    return chunk_texts, embeddings


def embed_query(query: str, model) -> np.ndarray:
    return model.encode([query], normalize_embeddings=True)[0]