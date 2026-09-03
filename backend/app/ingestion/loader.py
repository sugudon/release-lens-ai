from pathlib import Path

from langchain_community.document_loaders import TextLoader


KNOWLEDGE_BASE_DIR = Path("knowledge_base")

REQUIRED_METADATA = [
    "document_id",
    "document_type",
    "service",
    "source",
    "status",
]


def extract_metadata(file_path: Path) -> dict:
    metadata = {
        "source": str(file_path),
    }

    with file_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines or lines[0].strip() != "---":
        return metadata

    for line in lines[1:]:
        if line.strip() == "---":
            break

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        metadata[key.strip()] = value.strip()

    return metadata


def validate_document(document):
    missing = [
        field
        for field in REQUIRED_METADATA
        if not document.metadata.get(field)
    ]

    if missing:
        raise ValueError(
            f"Document "
            f"{document.metadata.get('source')} "
            f"is missing metadata: {missing}"
        )


def load_document(file_path: Path):
    loader = TextLoader(
        str(file_path),
        encoding="utf-8",
    )

    documents = loader.load()

    metadata = extract_metadata(file_path)

    for document in documents:
        document.metadata.update(metadata)
        validate_document(document)

    return documents


def load_knowledge_base():
    documents = []

    for file_path in KNOWLEDGE_BASE_DIR.rglob("*.md"):
        documents.extend(
            load_document(file_path)
        )

    return documents


if __name__ == "__main__":
    documents = load_knowledge_base()

    print(
        f"Successfully loaded "
        f"{len(documents)} documents."
    )

    for document in documents:
        print(
            document.metadata["document_id"],
            "|",
            document.metadata["document_type"],
            "|",
            document.metadata["service"],
        )