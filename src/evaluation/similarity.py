import numpy as np

def cosine_similarity(generated_answer: str, expected_answer: str, model) -> float:
    """
    Compute cosine similarity between generated answer and expected answer for qualitative evaluation.
    """
    if not generated_answer.strip() or not expected_answer.strip():
        return 0.0
    
    vectors = model.encode(
        [generated_answer, expected_answer],
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    gen_vec, exp_vec = vectors[0], vectors[1]

    return float(np.dot(gen_vec, exp_vec))