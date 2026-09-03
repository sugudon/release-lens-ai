from backend.app.rag.chain import create_rag_chain


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
    print("RELEASELENS STRUCTURED ANALYSIS")
    print("=" * 80)

    print("\nRisk Level:")
    print(result.risk_level)

    print("\nSummary:")
    print(result.summary)

    print("\nAffected Components:")
    for component in result.affected_components:
        print(f"- {component}")

    print("\nHistorical Incidents:")
    for incident in result.historical_incidents:
        print(f"- {incident}")

    print("\nArchitecture Decisions:")
    for adr in result.architecture_decisions:
        print(f"- {adr}")

    print("\nRisks:")
    for risk in result.risks:
        print(f"- {risk}")

    print("\nTesting Recommendations:")
    for test in result.testing_recommendations:
        print(f"- {test}")

    print("\nEvidence:")
    for evidence in result.evidence:
        print(f"- {evidence}")

    print("\nConfidence:")
    print(result.confidence)

    print("\nUncertainty:")
    for item in result.uncertainty:
        print(f"- {item}")


if __name__ == "__main__":
    main()