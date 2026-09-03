from backend.app.llm.release_chain import chain


def test_release_chain():
    result = chain.invoke(
        {
            "release_description": (
                "We are migrating Payment API v1 "
                "to Payment API v2."
            )
        }
    )

    assert isinstance(result, str)
    assert len(result) > 0