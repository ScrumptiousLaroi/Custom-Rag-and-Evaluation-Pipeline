from src.ingestion.loader import load_documents

SECTION_HEADERS = [
    "Summary:",
    "Key Findings:",
    "Evidence Snapshot:",
    "Interpretation:",
    "Limitations:",
    "Suggested Retrieval Keywords:"
]

def split_into_sections(text: str) -> list[tuple[str, str]]:
    positions: list[tuple[int, str]] = []
    for header in SECTION_HEADERS:
        idx = text.find(header)
        if idx != -1:
            positions.append((idx, header))
    positions.sort(key=lambda x: x[0])

    sections: list[tuple[str, str]] = []
    for i, (start_idx, header) in enumerate(positions):
        end_idx = positions[i + 1][0] if i + 1 < len(positions) else len(text)
        section_text = text[start_idx: end_idx].strip()
        if section_text:
            section_name = header.replace(":", "").strip()
            sections.append((section_name, section_text))
    return sections

def chunk_documents(documents: list[dict]) -> list[dict]:
    """
    Chunks the documents into sections based on predefined headers.
    Args:
        documents (list[str]): List of document strings to be chunked.
    Returns:
        list[dict]: List of dictionaries containing section headers and their corresponding content.
    """
    chunks: list[dict] = []

    for doc in documents:
        doc_id = doc.get("doc_id", "unknown_doc_id")
        text = doc.get("text", "").strip()
        source_path = doc.get("source_path", "")
        if not text:
            continue
        sections = split_into_sections(text)
        if not sections:
            sections = [("Full Document", text)]
        for idx, (section_name, section_text) in enumerate(sections, start = 1):
            chunk = {
                "chunk_id": f"{doc_id}_chunk_{idx:02d}",
                "doc_id": doc_id,
                "section_name": section_name,
                "chunk_text": section_text.strip(),
                "position_index": idx,
                "source_path": source_path
            }
            chunks.append(chunk)

    return chunks


            




