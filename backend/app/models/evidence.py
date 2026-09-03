from pydantic import BaseModel


class EvidenceItem(BaseModel):
    document_id: str
    document_type: str
    source: str
    claim: str