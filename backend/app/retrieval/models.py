from dataclasses import dataclass

from langchain_core.documents import Document


@dataclass
class RetrievedDocument:
    document: Document
    score: float