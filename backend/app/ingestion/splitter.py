from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from backend.app.ingestion.loader import (
    load_knowledge_base,
)

def add_chunk_metadata(chunks):
    for index, chunk in enumerate(chunks):
        document_id = chunk.metadata["document_id"]

        chunk.metadata["chunk_id"] = (
            f"{document_id}-chunk-{index + 1:03d}"
        )

    return chunks

def split_documents(
    documents,
    chunk_size=800,
    chunk_overlap=120,
):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_documents(documents)

    return add_chunk_metadata(chunks)


if __name__ == "__main__":
    documents = load_knowledge_base()

    chunks = split_documents(documents)

    print(f"Documents: {len(documents)}")
    print(f"Chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks[:5]):
        print("\n------------------------------")
        print(f"Chunk: {index + 1}")

        print(
            "Document ID:",
            chunk.metadata.get("document_id"),
        )

        print(
            "Document Type:",
            chunk.metadata.get("document_type"),
        )

        print(
            "Content length:",
            len(chunk.page_content),
        )

        print("Content:")
        print(chunk.page_content)