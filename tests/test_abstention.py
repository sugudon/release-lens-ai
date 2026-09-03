from backend.app.rag.chain import create_rag_chain


def test_unknown_when_evidence_is_insufficient():

    chain = create_rag_chain()

    result = chain.invoke(
        {
            "release_description": (
                "Will React 19 break our payment gateway?"
            )
        }
    )

    assert result.risk_level == "unknown"

    assert result.confidence == "low"

    assert len(result.uncertainty) > 0