from src.evaluation.questions import load_question_records
from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_documents
from src.retrieval.embedding import get_embedding_model, embed_chunks
from src.retrieval.retriever import retrieve_top_k
from src.generation.generation import build_context_from_results, generate_answer

from src.evaluation.evaluation_qualitative import (
    TOP_N_QUALITATIVE,
    build_qualitative_item,
    build_qualitative_template, save_qualitative_template, print_review_card
)

def initialize_rag():
    documents = load_documents()
    chunks = chunk_documents(documents)
    model = get_embedding_model()
    chunk_texts, chunk_embeddings = embed_chunks(chunks, model)
    return chunks, chunk_embeddings, model

def generate_answer_for_question(question_text, chunks, chunk_embeddings, model, top_k= 3):
    results = retrieve_top_k(question_text, chunks, chunk_embeddings, model, top_k=top_k)
    context = build_context_from_results(results)
    answer = generate_answer(question_text, context, model_name="google/flan-t5-small")
    return answer

if __name__ == "__main__":
    records = load_question_records()[:TOP_N_QUALITATIVE]
    chunks, chunk_embeddings, model = initialize_rag()

    items = []

    for record in records:
        print(f"Processing {record['question_id']}")
        generated_answer = generate_answer_for_question(
            record["question"], chunks, chunk_embeddings, model, top_k=3
        )
        item = build_qualitative_item(record, generated_answer)
        items.append(item)
        print_review_card(item)

    payload = build_qualitative_template(items)
    save_qualitative_template(payload)
    print("\nSaved qualitative template to outputs/qualitative_top5_template.json")