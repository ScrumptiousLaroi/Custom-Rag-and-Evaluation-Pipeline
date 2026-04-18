# Custom RAG and Evaluation Pipeline

This project builds a Retrieval-Augmented Generation (RAG) workflow on teen mental health documents and supports two evaluation modes:

- Quantitative evaluation: automatic cosine-similarity scoring against expected answers.
- Qualitative evaluation: automatic generation of a top-5 review template for human scoring.

The RAG setup uses a small teen mental health dataset. From this dataset, short markdown documents were prepared for retrieval, and a pre-made set of questions with expected answers was also prepared in the data folder for evaluation.

## Data Assets

- data/Teen_Mental_Health_Dataset.csv: source dataset used for this project.
- data/documents/: short derived markdown documents used by the RAG retriever.
- data/questions/Question and expected answers.md: pre-made evaluation questions and expected answers.

## 1) What This Project Does

The pipeline has four stages:

1. Ingestion: load markdown documents from data/documents.
2. Chunking: split each document into section-based chunks.
3. Retrieval + Generation: retrieve top-k chunks for a question, then generate a grounded answer using FLAN-T5.
4. Evaluation:
1. Quantitative: automatic semantic similarity metrics.
2. Qualitative: human rubric scoring using a generated JSON template.

## 2) Project Structure

- run_pipeline.py: quick single-query RAG demo.
- run_evaluation_quantitative.py: runs all evaluation questions and computes automatic metrics.
- run_evaluation_qualitative.py: runs top 5 questions and generates a human-review JSON template.
- src/ingestion/loader.py: loads documents.
- src/ingestion/chunker.py: builds section-based chunks.
- src/retrieval/embedding.py: sentence-transformer embedding utilities.
- src/retrieval/retriever.py: top-k retrieval by cosine-style dot product on normalized vectors.
- src/generation/generation.py: context formatting + grounded prompting + answer generation.
- src/evaluation/questions.py: reads and parses evaluation questions from markdown table.
- src/evaluation/similarity.py: semantic similarity for generated vs expected answer.
- src/evaluation/metrics.py: quantitative metric aggregation.
- src/evaluation/evaluation_qualitative.py: qualitative template and review-card helpers.
- outputs/qualitative_top5_template.json: generated qualitative review template.

## 3) Prerequisites

- Python 3.10+ (you are currently using Python 3.13.6).
- Hugging Face account and token.
- Internet connection for first-time model downloads.

Install dependencies:

	pip install -r requirements.txt

Important: src/evaluation/similarity.py uses scikit-learn. If it is not already installed, run:

	pip install scikit-learn

## 4) Hugging Face Authentication (First Step)

Before running generation scripts, authenticate once with Hugging Face.

Option A (recommended, CLI):

	huggingface-cli login

Paste your token when prompted.

Option B (environment variable):

	export HF_TOKEN=your_token_here

Then login from Python if needed by your environment setup.

Note: google/flan-t5-small is generally public, but authenticating avoids download/rate-limit friction and keeps setup consistent.

## 5) Run the RAG Pipeline (Single Query Demo)

Command:

	python run_pipeline.py

What it does:

1. Loads docs from data/documents.
2. Chunks docs by section headers.
3. Embeds chunks using all-MiniLM-L6-v2.
4. Retrieves top-2 chunks for a sample query.
5. Builds context and generates an answer with google/flan-t5-small.

Expected output:

- Terminal prints a generated answer for the sample query in run_pipeline.py.

## 6) Quantitative Evaluation (Automatic)

Command:

	python run_evaluation_quantitative.py

What this script does:

1. Loads all question records from data/questions/Question and expected answers.md.
2. Initializes RAG once.
3. Generates one answer per question.
4. Automatically computes cosine similarity between generated and expected answers.
5. Reports summary metrics.

Metrics computed automatically in src/evaluation/metrics.py:

- total_questions
- mean_similarity
- median_similarity
- pass_rate
- pass_threshold (default 0.60)

Interpretation:

- This is fully automated and reproducible.
- No manual scoring is needed for this part.

## 7) Qualitative Evaluation (Human in the Loop)

Command:

	python run_evaluation_qualitative.py

What this script does:

1. Loads the first 5 question records only (top-5 scope).
2. Generates answers using the same RAG setup.
3. Builds a qualitative template payload.
4. Saves it to outputs/qualitative_top5_template.json.
5. Prints a simple review card in terminal with:
1. Question
2. Expected answer
3. Generated answer

Important:

- Retrieved context is intentionally not displayed in the qualitative review card for simplicity.
- This part is semi-automatic: generation is automatic, scoring is manual.

## 8) How to Fill the Qualitative Template

Open outputs/qualitative_top5_template.json and fill each item under:

- qualitative_scores.coherence
- qualitative_scores.completeness
- qualitative_scores.factual_correctness
- reviewer_note

Use rubric scale 1-4:

- coherence:
1. 1 = hard to follow
2. 2 = partially clear
3. 3 = mostly clear
4. 4 = very clear
- completeness:
1. 1 = major missing parts
2. 2 = partial answer
3. 3 = mostly complete
4. 4 = fully complete
- factual_correctness:
1. 1 = mostly incorrect
2. 2 = mixed correctness
3. 3 = mostly correct
4. 4 = fully correct

This is human assessment, so a reviewer must manually assign these values.

## 9) End-to-End Workflow Summary

1. Authenticate with Hugging Face.
2. Install dependencies.
3. Run run_pipeline.py for a quick sanity check.
4. Run run_evaluation_quantitative.py for automatic metrics.
5. Run run_evaluation_qualitative.py to generate top-5 review template.
6. Manually fill outputs/qualitative_top5_template.json with rubric scores.

## 10) Common Issues

Issue: AttributeError: 'str' object has no attribute get in retriever.

- Cause: passing chunk_texts (list of strings) instead of chunks (list of dicts) to retrieve_top_k.
- Fix: ensure initialize_rag returns chunks to retrieval.

Issue: ModuleNotFoundError for sklearn.

- Fix: pip install scikit-learn

Issue: typing Python code directly in shell gives command not found.

- Example: TOP_N_QUALITATIVE = 5 in terminal returns exit code 127.
- Fix: put Python statements inside .py files, then run scripts with python.

## 11) Suggested Next Improvements

- Save quantitative scored results to outputs/quantitative_results.json.
- Add a small script to compute averages from filled qualitative JSON.
- Add retry/validation for short generated answers to improve quality.
