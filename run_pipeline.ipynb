from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_documents
from src.retrieval.embedding import get_embedding_model, embed_chunks
from src.retrieval.retriever import retrieve_top_k
from src.generation.generation import generate_answer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


documents = load_documents()
chunks = chunk_documents(documents)

model = get_embedding_model()
chunk_texts, chunk_embeddings = embed_chunks(chunks, model)


query = "Is high level screen time better or risks explained in the document?"
results = retrieve_top_k(query, chunks, chunk_embeddings, model, top_k=2)

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base") 

answer = generate_answer(query, results, model)
print("\n Generated Answer:" + answer)