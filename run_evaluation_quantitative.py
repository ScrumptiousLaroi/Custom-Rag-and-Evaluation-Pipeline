from src.evaluation.questions import load_question_records
from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_documents
from src.retrieval.embedding import get_embedding_model, embed_chunks
from src.retrieval.retriever import retrieve_top_k
from src.generation.generation import build_context_from_results, generate_answer
from src.evaluation.metrics import evaluate_quantitative

def initialize_rag():
    documents = load_documents()
    chunks = chunk_documents(documents)
    model = get_embedding_model()
    chunk_texts, chunk_embeddings = embed_chunks(chunks, model)
    return documents, chunks, model, chunk_texts, chunk_embeddings

def generate_answer_for_question(question_text: str, chunks, chunk_embeddings, model, top_k):
    results = retrieve_top_k(question_text, chunks, chunk_embeddings, model, top_k=top_k)
    context = build_context_from_results(results)
    answer = generate_answer(question_text, context, model_name="google/flan-t5-small")
    return answer, results


if __name__ == "__main__":
    question_records = load_question_records()
    documents, chunks, model, chunk_texts, chunk_embeddings = initialize_rag()

    all_results = []

    for record in question_records:
        print(f"Processing {record['question_id']}")

        generated_answer, retrieved_results = generate_answer_for_question(
            record["question"],
            chunks,
            chunk_embeddings,
            model,
            top_k=3
        )

        all_results.append({
            "question_id": record["question_id"],
            "question": record["question"],
            "expected_answer": record["expected_answer"],
            "generated_answer": generated_answer,
            "retrieved_chunk_ids": [r["chunk_id"] for r in retrieved_results],
            "retrieved_doc_ids": [r["doc_id"] for r in retrieved_results]
        })

    print("Processed questions:", len(all_results))

    # Evaluate the results quantitatively
    scored_results, summary = evaluate_quantitative(all_results, model)

    print("\nQuantitative Summary:")
    print(summary)
    