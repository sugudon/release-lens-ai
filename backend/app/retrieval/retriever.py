from typing import Any

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from pydantic import ConfigDict

from backend.app.db.search import similarity_search
from backend.app.ingestion.embeddings import embed_query


class ReleaseLensRetriever(BaseRetriever):
    top_k: int = 5
    similarity_threshold: float | None = None
    document_type: str | None = None
    service: str | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def _get_relevant_documents(
        self,
        query: str,
        *,
        run_manager: Any,
    ) -> list[Document]:

        query_vector = embed_query(query)

        results = similarity_search(
            query_vector=query_vector,
            limit=self.top_k,
            document_type=self.document_type,
            service=self.service,
        )

        documents = []

        for result in results:

            distance = float(result["distance"])

            if (
                self.similarity_threshold is not None
                and distance > self.similarity_threshold
            ):
                continue

            documents.append(
                Document(
                    page_content=result["content"],
                    metadata={
                        "document_id": result["document_id"],
                        "chunk_id": result["chunk_id"],
                        "document_type": result["document_type"],
                        "service": result["service"],
                        "source": result["source"],
                        "status": result["status"],
                        "distance": distance,
                    },
                )
            )

        return documents