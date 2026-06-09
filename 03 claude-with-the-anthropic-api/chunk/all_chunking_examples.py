"""Illustrative chunking examples for Claude, LangChain, and LangGraph."""

import re
from typing import List, TypedDict

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def chunk_by_size(text: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = end - overlap
    return chunks

def chunk_by_structure_markdown(text: str) -> List[str]:
    sections = re.split(r"(?m)^## ", text)
    cleaned = [s.strip() for s in sections if s.strip()]
    return cleaned

def chunk_by_sentence(text: str, max_sentences: int = 3, overlap_sentences: int = 1) -> List[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks = []
    start = 0
    step = max(1, max_sentences - overlap_sentences)
    while start < len(sentences):
        end = min(start + max_sentences, len(sentences))
        chunks.append(" ".join(sentences[start:end]))
        if end == len(sentences):
            break
        start += step
    return chunks

# Semantic chunking is shown conceptually; real use typically requires embeddings.
def pseudo_semantic_chunk(text: str) -> List[str]:
    paragraphs = [p.strip() for p in text.split("

") if p.strip()]
    return paragraphs

if __name__ == "__main__":
    text = load_text("sample_input.txt")
    print("SIZE:", chunk_by_size(text)[:2])
    print("STRUCTURE:", chunk_by_structure_markdown(text)[:2])
    print("SENTENCE:", chunk_by_sentence(text)[:2])
    print("SEMANTIC:", pseudo_semantic_chunk(text)[:2])