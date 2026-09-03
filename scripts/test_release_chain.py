from backend.app.llm.release_chain import chain


release_description = """
We are migrating the payment integration from Payment API v1
to Payment API v2. The new API changes the payment request format
and introduces a different retry behavior.
"""


result = chain.invoke(
    {
        "release_description": release_description
    }
)


print(result)