import numpy as np
from src.evaluation.similarity import cosine_similarity

def evaluate_quantitative(results: list[dict], model, pass_threshold: float=0.60):
    scored_results = []

    for row in results:
        score = cosine_similarity(
            row["generated_answer"],
            row["expected_answer"],
            model
        )

        enriched = dict(row)
        enriched["cosine_similarity"] = round(score, 4)
        enriched["passed"] = score >= pass_threshold
        scored_results.append(enriched)

    if not scored_results:
        summary = {
            "total_questions": 0,
            "mean_similarity": 0.0,
            "median_similarity": 0.0,
            "pass_rate": 0.0,
            "pass_threshold": pass_threshold
        }
        return scored_results, summary
    
    scores = [r["cosine_similarity"] for r in scored_results]
    passes = [1 if r["passed"] else 0 for r in scored_results]

    summary= {
        "total_questions": len(scored_results),
        "mean_similarity": round(float(np.mean(scores)), 4),
        "median_similarity": round(float(np.median(scores)), 4),
        "pass_rate": round(float(np.mean(passes)), 4),
        "pass_threshold": pass_threshold
    }
    return scored_results, summary
    
