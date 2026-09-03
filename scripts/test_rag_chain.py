from backend.app.rag.chain import (
    create_rag_chain,
)


def main():

    release_description = """
Upgrade Payment API from v1 to v2.

Change payment retry behavior from 3 retries
to 5 retries.

The change will be deployed to production next week.
"""

    chain = create_rag_chain()

    result = chain.invoke(
        {
            "release_description": release_description
        }
    )

    print("\n")
    print("=" * 80)
    print("RELEASELENS ANALYSIS")
    print("=" * 80)
    print("\n")

    print(result)


if __name__ == "__main__":
    main()