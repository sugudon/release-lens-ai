from backend.app.rag.chain import create_rag_chain


def analyze_release(release_description: str):
    chain = create_rag_chain()

    return chain.invoke(
        {
            "release_description": release_description
        }
    )