from langsmith import evaluate

from backend.app.rag.chain import create_rag_chain

from evaluation.evaluators import (
    evidence_recall,
    impact_detection,
    risk_classification,
    testing_recommendations,
    abstention_quality,
    citation_correctness,
)


DATASET_NAME = "release-lens-ai-evaluation-v1"


chain = create_rag_chain()


def target(inputs: dict) -> dict:

    result = chain.invoke(
        {
            "release_description": inputs[
                "release_description"
            ]
        },
        config={
            "run_name": "ReleaseLens Evaluation",
            "tags": [
                "evaluation",
                "release-analysis",
            ],
            "metadata": {
                "application": "release-lens-ai",
                "evaluation": "v1",
            },
        },
    )

    return {
        "summary": result.summary,
        "affected_components": result.affected_components,
        "risks": result.risks,
        "testing_recommendations": (
            result.testing_recommendations
        ),
        "evidence": result.evidence,
        "confidence": result.confidence,
    }


def main():

    evaluators = [
        evidence_recall,
        impact_detection,
        risk_classification,
        testing_recommendations,
        abstention_quality,
        citation_correctness,
    ]

    results = evaluate(
        target,
        data=DATASET_NAME,
        evaluators=evaluators,
        experiment_prefix="release-lens-v1",
        max_concurrency=2,
    )

    print(results)


if __name__ == "__main__":
    main()