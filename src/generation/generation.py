from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


def build_context_from_results(results: list[dict]) -> str:
    """
    Assemble retrieved chunks into a single context string.
    """

    if not results:
        return "No relevant context found."
    
    context = ""

    for r in results:
        context += f"\n[{r['chunk_id']}] ({r['section_name']})\n"
        context += r['chunk_text'] + "\n"

    return context

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


def generate_answer(question: str, context: str, model_name: str = "google/flan-t5-base") -> str:
    """
    Generate grounded answer using a small q and a text model.
    """
   

    prompt = build_grounded_prompt(question, context)

    generator = pipeline("text2text-generation", model=model_name)
    result = generator(prompt, max_length=512, do_sample=False) # do sample false only generates one result

    return result[0]['generated_text']
