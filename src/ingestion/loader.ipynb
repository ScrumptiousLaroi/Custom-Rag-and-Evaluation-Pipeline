import os

def load_documents():

    documents_path = os.path.join(os.path.expanduser("/Volumes/Puru External Drive/Work/Conversly AI/Assignment 3/data/"), "documents")
    print(documents_path)
    documents = []
    if os.path.exists(documents_path):
        items = os.listdir(documents_path)
        for item in items:
            if item.startswith(".") or not item.endswith(".md"):
                continue
            doc_id = os.path.splitext(item)[0]
            file_path = os.path.join(documents_path, item)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read().strip()
            if not text:
                continue
            doc = {
                "doc_id": doc_id,
                "text": text,
                "source_path": file_path
            }
            documents.append(doc)
        print(f"Loaded {len(documents)} documents.")
    else:
        print("Directory does not exist.")
    
    return documents


if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} docs")
    if docs:
        print(docs[0]["doc_id"], len(docs[0]["text"]))
