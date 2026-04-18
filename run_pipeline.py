from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_documents
from src.retrieval.embedding import get_embedding_model, embed_chunks
from src.retrieval.retriever import retrieve_top_k

documents = load_documents()
chunks = chunk_documents(documents)

model = get_embedding_model()
chunk_texts, chunk_embeddings = embed_chunks(chunks, model)


query = "Is high level screen time better or risks explained in the document?"
results = retrieve_top_k(query, chunks, chunk_embeddings, model, top_k=2)


print("\nQuery:", query)

for r in results:
    print(f"[{r['rank']}] {r['chunk_id']} | {r['section_name']} | score={r['score']:.4f}")
    print(r["chunk_text"][:180], "\n")