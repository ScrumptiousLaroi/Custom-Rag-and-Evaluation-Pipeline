def build_context_from_results(results: list[dict]) -> str:
    """
    Assemble retrieved chunks into a single context string.
    """

    if not results:
        return "No relevant context found."

    grouped_results: dict[str, list[dict]] = {}
    for r in results:
        grouped_results.setdefault(r.get("doc_id", "unknown_doc_id"), []).append(r)

    context_parts: list[str] = []
    for doc_id, doc_results in grouped_results.items():
        context_parts.append(f"Source Document: {doc_id}")
        for r in doc_results:
            context_parts.append(f"  - {r['section_name']} [{r['chunk_id']}]")
            context_parts.append(r["chunk_text"])

    return "\n".join(context_parts)

def build_grounded_prompt(question: str, context: str) -> str:
    """
    Build a strict prompt so that model is forced to answer from the documents and not general knowledge.
    """

    prompt = f"""
    You are a grounded assistant. Answer the questions question using ONLY the context provided below.
    Do not use external knowledge. If the answer cannot be found in the context, respond: "Insufficient context from retrieved documents."

    Context:
    {context}

    Question: {question}

    Answer:"""

    return prompt


def generate_answer(question: str, context: str, model_name: str = "google/flan-t5-small") -> str:
    """
    Generate grounded answer using a small text-to-text pipeline.
    """

    from transformers import pipeline

    prompt = build_grounded_prompt(question, context)
    generator = pipeline("text2text-generation", model=model_name)
    result = generator(prompt, max_length=512, do_sample=False)

    return result[0]["generated_text"]
