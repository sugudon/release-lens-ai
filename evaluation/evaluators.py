def _normalise(value):
    if value is None:
        return []

    if isinstance(value, str):
        return [value.lower()]

    return [
        str(item).lower()
        for item in value
    ]


def _contains_expected(actual, expected):
    actual_values = _normalise(actual)

    matched = 0

    for expected_value in expected:
        expected_value = expected_value.lower()

        if any(
            expected_value in actual_value
            for actual_value in actual_values
        ):
            matched += 1

    if not expected:
        return 1.0

    return matched / len(expected)


def evidence_recall(
    inputs: dict,
    outputs: dict,
    reference_outputs: dict,
):
    expected = reference_outputs.get(
        "expected_evidence",
        [],
    )

    actual = outputs.get(
        "evidence",
        [],
    )

    score = _contains_expected(
        actual,
        expected,
    )

    return {
        "key": "evidence_recall",
        "score": score,
    }


def impact_detection(
    inputs: dict,
    outputs: dict,
    reference_outputs: dict,
):
    expected = reference_outputs.get(
        "expected_impact",
        [],
    )

    actual = outputs.get(
        "affected_components",
        [],
    )

    score = _contains_expected(
        actual,
        expected,
    )

    return {
        "key": "impact_detection",
        "score": score,
    }


def risk_classification(
    inputs: dict,
    outputs: dict,
    reference_outputs: dict,
):
    expected = reference_outputs.get(
        "expected_risk"
    )

    actual = outputs.get(
        "risks",
        []
    )

    if not expected:
        return {
            "key": "risk_classification",
            "score": 1.0,
        }

    if not actual:
        return {
            "key": "risk_classification",
            "score": 0.0,
        }

    actual_values = _normalise(actual)

    expected_value = str(expected).lower()

    score = (
        1.0
        if any(
            expected_value in actual_value
            for actual_value in actual_values
        )
        else 0.0
    )

    return {
        "key": "risk_classification",
        "score": score,
    }

def testing_recommendations(
    inputs: dict,
    outputs: dict,
    reference_outputs: dict,
):
    expected = reference_outputs.get(
        "expected_testing",
        [],
    )

    actual = outputs.get(
        "testing_recommendations",
        [],
    )

    score = _contains_expected(
        actual,
        expected,
    )

    return {
        "key": "testing_recommendations",
        "score": score,
    }


def abstention_quality(
    inputs: dict,
    outputs: dict,
    reference_outputs: dict,
):
    expected_risk = reference_outputs.get(
        "expected_risk"
    )

    actual_risk = outputs.get(
        "risk"
    )

    if expected_risk != "unknown":
        return {
            "key": "abstention_quality",
            "score": 1.0,
        }

    score = (
        1.0
        if actual_risk == "unknown"
        else 0.0
    )

    return {
        "key": "abstention_quality",
        "score": score,
    }

def citation_correctness(
    inputs: dict,
    outputs: dict,
    reference_outputs: dict,
):
    expected = reference_outputs.get(
        "expected_evidence",
        [],
    )

    actual = outputs.get(
        "evidence",
        [],
    )

    score = _contains_expected(
        actual,
        expected,
    )

    return {
        "key": "citation_correctness",
        "score": score,
    }