from pathlib import Path

"""
Functions for loading and parsing question data from a Markdown file.
"""

QUESTIONS_MD = Path("data/questions/Question and expected answers.md")

def load_question_file_lines(QUESTIONS_MD: Path) -> list[str]:

    if not QUESTIONS_MD.exists():
        raise FileNotFoundError(f"Question file not found: {QUESTIONS_MD}")
    
    with QUESTIONS_MD.open("r", encoding="utf-8") as f:
        lines = f.readlines()
        return lines
    

def keep_table_lines(lines: list[str]) -> list[str]:
    return [ln for ln in lines if ln.strip().startswith("|")]  

def is_data_row(line: str) -> bool:
    low = line.lower()

    if "question_id" in low and "expected_answer" in low:
        return False
    if ":---" in line:
        return False
    return True  


def parse_row(line: str) -> list[str]:
    parts = [p.strip() for p in line.strip().split("|")]
    parts = [p for p in parts if p != ""]
    return parts


def row_to_record(parts: list[str]) -> dict | None:
    if len(parts) != 9:
        return None

    return {
        "question_id": parts[0],
        "question": parts[3],
        "expected_answer": parts[4],
    }


def load_question_records(md_path: Path = QUESTIONS_MD) -> list[dict]:
    lines = load_question_file_lines(md_path)
    table_lines = keep_table_lines(lines)

    records = []
    for ln in table_lines:
        if not is_data_row(ln):
            continue
        parts = parse_row(ln)
        record = row_to_record(parts)
        if record is not None:
            records.append(record)

    return records

if __name__ == "__main__":
    records = load_question_records()
    print("Total records:", len(records))
    if records:
        print("First:", records[0])
        print("Last:", records[-1])
