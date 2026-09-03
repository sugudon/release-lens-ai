from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from backend.app.models.release_analysis import (
    ReleaseAnalysis,
)

from backend.app.rag.prompts import (
    RELEASE_ANALYSIS_PROMPT,
)

from backend.app.retrieval.factory import (
    create_retriever,
)

from backend.app.retrieval.query_processor import (
    process_query,
)


# =========================================================
# Configuration
# =========================================================

# IMPORTANT:
# This value is currently not used for filtering here.
# Filtering is handled by the retriever.
#
# Keep threshold configuration in one place:
# backend/app/retrieval/factory.py / retriever.py


# =========================================================
# Document Formatting
# =========================================================

def format_documents(
    documents: list[Document],
) -> str:

    if not documents:
        return (
            "No relevant engineering evidence was retrieved."
        )

    formatted_documents = []

    for document in documents:

        metadata = document.metadata

        document_id = metadata.get(
            "document_id",
            "UNKNOWN",
        )

        document_type = metadata.get(
            "document_type",
            "UNKNOWN",
        )

        service = metadata.get(
            "service",
            "UNKNOWN",
        )

        source = metadata.get(
            "source",
            "UNKNOWN",
        )

        # Your retriever currently provides
        # "distance", not "similarity_score".
        distance = metadata.get(
            "distance"
        )

        distance_text = (
            f"{distance:.4f}"
            if isinstance(distance, (int, float))
            else "UNKNOWN"
        )

        formatted_documents.append(
            f"""
[DOCUMENT]
document_id: {document_id}
document_type: {document_type}
service: {service}
source: {source}
distance: {distance_text}

content:
{document.page_content}
[/DOCUMENT]
"""
        )

    return "\n".join(formatted_documents)


# =========================================================
# Retrieval Assessment
# =========================================================

def assess_retrieval(
    documents: list[Document],
) -> tuple[bool, str, list[Document]]:

    """
    Determine whether the retriever returned
    usable engineering evidence.

    The similarity threshold itself is already
    handled inside ReleaseLensRetriever.

    Therefore this function checks whether
    usable documents remain after retrieval.
    """

    if not documents:

        return (
            False,
            "No relevant engineering evidence was retrieved.",
            [],
        )

    valid_documents = []

    for document in documents:

        distance = document.metadata.get(
            "distance"
        )

        if isinstance(distance, (int, float)):

            valid_documents.append(
                document
            )

    if not valid_documents:

        return (
            False,
            (
                "Retrieved documents did not contain "
                "valid similarity information."
            ),
            [],
        )

    return (
        True,
        "Sufficient relevant evidence was retrieved.",
        valid_documents,
    )


# =========================================================
# Deterministic Abstention
# =========================================================

def create_abstention_result(
    reason: str,
) -> ReleaseAnalysis:

    return ReleaseAnalysis(

        risk_level="unknown",

        summary=(
            "The knowledge base does not contain "
            "sufficient evidence to reliably assess "
            "this release."
        ),

        affected_components=[],

        historical_incidents=[],

        architecture_decisions=[],

        risks=[],

        testing_recommendations=[
            (
                "Validate the proposed change in a "
                "controlled test environment."
            )
        ],

        recommended_actions=[
            (
                "Collect additional engineering evidence "
                "before making a production release decision."
            )
        ],

        evidence=[],

        confidence="low",

        uncertainty=[
            reason,
        ],
    )


# =========================================================
# Create RAG Chain
# =========================================================

def create_rag_chain():

    # -----------------------------------------------------
    # Retriever
    # -----------------------------------------------------

    retriever = create_retriever(
        top_k=5,
    )

    # -----------------------------------------------------
    # Chat Model
    # -----------------------------------------------------

    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    # -----------------------------------------------------
    # Structured Output
    # -----------------------------------------------------

    structured_model = model.with_structured_output(
        ReleaseAnalysis
    )

    # -----------------------------------------------------
    # Query Processing + Retrieval
    # -----------------------------------------------------

    def retrieve_and_assess(
        inputs: dict,
    ) -> dict:

        # ---------------------------------------------
        # Original user request
        # ---------------------------------------------

        release_description = inputs[
            "release_description"
        ]

        # ---------------------------------------------
        # Phase 12:
        # Convert user query into a retrieval-oriented
        # query while preserving the original request.
        # ---------------------------------------------

        processed_query = process_query(
            release_description
        )

        # ---------------------------------------------
        # IMPORTANT:
        # Use ONLY retrieval_query for vector search.
        # ---------------------------------------------

        documents = retriever.invoke(
            processed_query.retrieval_query
        )

        # ---------------------------------------------
        # Assess retrieved evidence
        # ---------------------------------------------

        (
            sufficient_evidence,
            reason,
            relevant_documents,
        ) = assess_retrieval(
            documents
        )

        return {

            # Original user request
            "release_description":
                release_description,

            # Internal retrieval query
            "retrieval_query":
                processed_query.retrieval_query,

            # Concepts generated by query processor
            "query_concepts":
                processed_query.concepts,

            # Retrieved documents
            "documents":
                relevant_documents,

            # Evidence assessment
            "sufficient_evidence":
                sufficient_evidence,

            "reason":
                reason,
        }

    # -----------------------------------------------------
    # Final RAG Invocation
    # -----------------------------------------------------

    def invoke_chain(
        inputs: dict,
    ) -> ReleaseAnalysis:

        retrieval_result = retrieve_and_assess(
            inputs
        )

        # -------------------------------------------------
        # Deterministic Abstention
        # -------------------------------------------------

        if not retrieval_result[
            "sufficient_evidence"
        ]:

            return create_abstention_result(
                retrieval_result["reason"]
            )

        # -------------------------------------------------
        # Format Retrieved Evidence
        # -------------------------------------------------

        context = format_documents(
            retrieval_result["documents"]
        )

        # -------------------------------------------------
        # Prompt Input
        # -------------------------------------------------

        prompt_input = {

            # IMPORTANT:
            # The LLM receives the ORIGINAL request,
            # not the rewritten retrieval query.
            "release_description":
                retrieval_result[
                    "release_description"
                ],

            # The LLM receives actual retrieved
            # engineering evidence.
            "context":
                context,
        }

        # -------------------------------------------------
        # Prompt → Structured LLM
        # -------------------------------------------------

        chain = (
            RELEASE_ANALYSIS_PROMPT
            | structured_model
        )

        result = chain.invoke(
            prompt_input
        )

        # -------------------------------------------------
        # Validate Citations
        # -------------------------------------------------

        retrieved_document_ids = {
            document.metadata.get(
                "document_id"
            )
            for document
            in retrieval_result[
                "documents"
            ]
        }

        validated_evidence = []

        for evidence in result.evidence:

            if (
                evidence.document_id
                in retrieved_document_ids
            ):

                validated_evidence.append(
                    evidence
                )

        result.evidence = (
            validated_evidence
        )

        # -------------------------------------------------
        # Final Grounding Check
        # -------------------------------------------------

        if not result.evidence:

            result.risk_level = "unknown"

            result.confidence = "low"

            result.uncertainty.append(
                (
                    "The generated analysis did not "
                    "contain validated supporting evidence."
                )
            )

        return result

    # -----------------------------------------------------
    # Return Runnable
    # -----------------------------------------------------

    return RunnableLambda(
        invoke_chain
    )