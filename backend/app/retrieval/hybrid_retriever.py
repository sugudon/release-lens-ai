from typing import Any

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from pydantic import ConfigDict

from backend.app.retrieval.hybrid_search import (
    hybrid_search,
)


class HybridReleaseLensRetriever(
    BaseRetriever
):

    top_k: int = 5

    document_type: str | None = None

    service: str | None = None

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )

    def _get_relevant_documents(
        self,
        query: str,
        *,
        run_manager: Any,
    ) -> list[Document]:

        return hybrid_search(
            query=query,
            limit=self.top_k,
            document_type=self.document_type,
            service=self.service,
        ) 