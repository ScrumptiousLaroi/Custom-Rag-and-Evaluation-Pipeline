from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_documents
from src.retrieval.embedding import get_embedding_model, embed_chunks
from src.retrieval.retriever import retrieve_top_k
from src.generation.generation import build_context_from_results, generate_answer


documents = load_documents()
chunks = chunk_documents(documents)

model = get_embedding_model()
chunk_texts, chunk_embeddings = embed_chunks(chunks, model)


query = " Which social media platform is associated with the highest average anxiety scores among teens? "
results = retrieve_top_k(query, chunks, chunk_embeddings, model, top_k=2)

context = build_context_from_results(results)
answer = generate_answer(query, context, model_name="google/flan-t5-small")
print("\n Generated Answer:" + answer)