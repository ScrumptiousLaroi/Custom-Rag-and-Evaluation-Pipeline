import json
from pathlib import Path

TOP_N_QUALITATIVE = 5 #to consider only top 5 questions for now,
QUALITATIVE_OUTPUT_PATH = Path("outputs/qualitative_top5_template.json")

def build_qualitative_item(record, generated_answer):
    return {
        "question_id": record["question_id"],
        "question": record["question"],
        "expected_answer": record["expected_answer"],
        "generated_answer": generated_answer,
        "qualitative_scores": {
            "coherence": None,
            "completeness": None,
            "factual_correctness": None,
        },
        "reviewer_note": ""
    }

def build_qualitative_template(items):
    return{
        "assessment_name": "Qualitative Evaluation Template",
        "rubric_scale": {
        "coherence":"1-4",
        "completeness": "1-4",
        "factual_correctness": "1-4",
        },
        "items": items
    }

def save_qualitative_template(payload, output_path=QUALITATIVE_OUTPUT_PATH):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

def print_review_card(item):
    print("\n" + "=" * 80)
    print(f"Question ID: {item['question_id']}")
    print(f"Question: {item['question']}")
    print("\nExpected Answer:")
    print(item["expected_answer"])
    print("\nGenerated Answer:")
    print(item["generated_answer"])
    print("=" * 80)



