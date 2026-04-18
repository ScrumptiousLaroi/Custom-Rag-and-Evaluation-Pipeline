import numpy as np
from src.retrieval.embedding import get_embedding_model, embed_chunks, embed_query


def retrieve_top_k(query: str, chunks: list[dict], chunk_embeddings: np.ndarray, model, top_k: int = 3) -> list[dict]:
    if not query.strip():
        return []
    if len(chunks) == 0:
        return []
    
    k = min(top_k, len(chunks))
    query_vec = embed_query(query, model)
    scores = chunk_embeddings @ query_vec
    top_k_indices = np.argsort(scores)[-k:][::-1] #top k in decending order

    results = []

    for rank, idx in enumerate(top_k_indices, start = 1):
        c = chunks[int(idx)]
        results.append({
            "rank": rank,
            "score": float(scores[idx]),
            "chunk_id": c.get("chunk_id"),
            "doc_id": c.get("doc_id"),
            "section_name": c.get("section_name"),
            "chunk_text": c.get("chunk_text", ""),
        })

    return results
