from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

from backend.app.ingestion.loader import (
    load_knowledge_base,
)

from backend.app.ingestion.splitter import (
    split_documents,
)


load_dotenv()


EMBEDDING_MODEL = "text-embedding-3-small"


def create_embedding_model():
    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
    )


def embed_documents(chunks):
    model = create_embedding_model()

    texts = [
        chunk.page_content
        for chunk in chunks
    ]

    return model.embed_documents(texts)


def embed_query(query: str):
    model = create_embedding_model()

    return model.embed_query(query)


def main():
    documents = load_knowledge_base()

    chunks = split_documents(
        documents,
        chunk_size=800,
        chunk_overlap=120,
    )

    vectors = embed_documents(chunks)

    print(f"Documents: {len(documents)}")
    print(f"Chunks: {len(chunks)}")
    print(f"Vectors: {len(vectors)}")

    if vectors:
        print(
            f"Embedding dimensions: "
            f"{len(vectors[0])}"
        )

    query = (
        "What caused the previous "
        "payment timeout?"
    )

    query_vector = embed_query(query)

    print(
        f"Query dimensions: "
        f"{len(query_vector)}"
    )


if __name__ == "__main__":
    main()