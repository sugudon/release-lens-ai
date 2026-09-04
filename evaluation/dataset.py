from dotenv import load_dotenv
from langsmith import Client


load_dotenv()

DATASET_NAME = "release-lens-ai-evaluation-v1"


EVALUATION_CASES = [
    {
        "inputs": {
            "release_description": """
Upgrade Payment API from v1 to v2.

Change payment retry behavior from 3 retries
to 5 retries.

The change will be deployed to production next week.
"""
        },
        "outputs": {
            "expected_evidence": [
                "ADR-003",
                "ARCH-003",
            ],
            "expected_impact": [
                "Payment",
                "Checkout",
            ],
            "expected_risk": "high",
            "expected_testing": [
                "load testing",
                "integration testing",
                "regression testing",
            ],
        },
        "metadata": {
            "category": "multi_document",
            "difficulty": "medium",
        },
    },
    {
        "inputs": {
            "release_description": """
What historical incident is related to payment retry configuration?
"""
        },
        "outputs": {
            "expected_evidence": [
                "INC-1024",
            ],
            "expected_impact": [
                "Payment",
            ],
            "expected_risk": "high",
        },
        "metadata": {
            "category": "historical_incident",
            "difficulty": "easy",
        },
    },
    {
        "inputs": {
            "release_description": """
What testing should be performed when changing
payment retry behavior?
"""
        },
        "outputs": {
            "expected_evidence": [
                "testing",
                "ADR-003",
            ],
            "expected_testing": [
                "load testing",
                "integration testing",
            ],
        },
        "metadata": {
            "category": "testing_recommendation",
            "difficulty": "medium",
        },
    },
    {
        "inputs": {
            "release_description": """
Change the font size on the internal documentation page.
"""
        },
        "outputs": {
            "expected_evidence": [],
            "expected_impact": [],
            "expected_risk": "unknown",
        },
        "metadata": {
            "category": "no_evidence",
            "difficulty": "easy",
        },
    },
    {
        "inputs": {
            "release_description": """
We are changing the retry configuration.
What could be affected?
"""
        },
        "outputs": {
            "expected_evidence": [
                "payment",
                "checkout",
            ],
            "expected_impact": [
                "Payment",
                "Checkout",
            ],
        },
        "metadata": {
            "category": "ambiguous",
            "difficulty": "hard",
        },
    },
    {
        "inputs": {
            "release_description": """
What does ADR-003 say about the Payment API migration?
"""
        },
        "outputs": {
            "expected_evidence": [
                "ADR-003",
            ],
        },
        "metadata": {
            "category": "exact_identifier",
            "difficulty": "easy",
        },
    },
    {
        "inputs": {
            "release_description": """
What could be affected by Payment API v2 migration?
"""
        },
        "outputs": {
            "expected_evidence": [
                "ADR-003",
                "ARCH-003",
            ],
            "expected_impact": [
                "Payment",
                "Checkout",
            ],
        },
        "metadata": {
            "category": "easy_retrieval",
            "difficulty": "easy",
        },
    },
]


def main():
    client = Client()

    dataset = client.create_dataset(
        dataset_name=DATASET_NAME,
        description=(
            "ReleaseLens AI evaluation dataset for "
            "retrieval, risk analysis, evidence grounding, "
            "testing recommendations, and abstention."
        ),
    )

    client.create_examples(
        dataset_id=dataset.id,
        examples=EVALUATION_CASES,
    )

    print(f"Created dataset: {dataset.name}")
    print(f"Dataset ID: {dataset.id}")
    print(f"Examples: {len(EVALUATION_CASES)}")


if __name__ == "__main__":
    main()