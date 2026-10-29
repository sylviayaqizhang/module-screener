import numpy as np
import pytest
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from module_screener.analysis.generate_demo_data import (
    generate_dataset,
    calculate_module_scores,
    recommend_level,
    generate_student,
)

from module_screener.analysis.summary import (
    extract_module_scores,
    summarise_scores,
)

from module_screener.analysis.visualisation import (
    plot_familiarity_ability,
    plot_composite_distribution,
    plot_recommendation_boxplot,
)



# generate a sample dataset for unit tests
@pytest.fixture
def sample_dataset():
    rng = np.random.default_rng(88)
    return generate_dataset(rng, n_students=5)


# test correct calculation of familiarity, ability and composite scores
def test_calculate_module_scores():
    questions = {
        "Q1": {"familiarity": 2, "ability": 3},
        "Q2": {"familiarity": 4, "ability": 1}
    }

    scores = calculate_module_scores(questions)

    assert scores["mean_familiarity"] == 3
    assert scores["mean_ability"] == 2
    assert scores["composite_score"] == 2.5

# test recommendations above, below and at the threshold
def test_recommend_level():
    # check above threshold
    assert recommend_level(3.0) == "advanced"

    # check below threshold
    assert recommend_level(2.0) == "intro"

    # check exactly at threshold
    assert recommend_level(2.5) == "advanced"

# test student record structure and required fields
def test_student_complete_structure():
    rng = np.random.default_rng(88)
    student = generate_student(1, rng)

    assert student["id"] == "001"

    for module in ["python", "math"]:
        module_data = student["modules"][module]

        assert "questions" in module_data
        assert "scores" in module_data
        assert "recommendation" in module_data

        assert len(module_data["questions"]) == 5

        assert module_data["recommendation"] in ("intro", "advanced")

# test reproducibility using the same random seed
def test_dataset_reproducibility():
    rng1 = np.random.default_rng(88)
    rng2 = np.random.default_rng(88)

    dataset1 = generate_dataset(rng1)
    dataset2 = generate_dataset(rng2)

    assert dataset1 == dataset2


# test extraction of module scores from student records
def test_extract_module_scores(sample_dataset):
    scores = extract_module_scores(sample_dataset, "python")

    assert len(scores["familiarity"]) == 5
    assert len(scores["ability"]) == 5
    assert len(scores["composite"]) == 5

    assert scores["familiarity"][0] == sample_dataset[0]["modules"]["python"]["scores"]["mean_familiarity"]


# test descriptive statistics against known values
def test_summarise_scores():
    values = [1, 2, 3, 4, 5]

    summary = summarise_scores(values)

    assert summary["n"] == 5
    assert summary["mean"] == 3
    assert summary["median"] == 3
    assert summary["min"] == 1
    assert summary["max"] == 5
    assert summary["sd"] == pytest.approx(1.58113883)

# test that python and maths scores are extracted independently
def test_module_separation(sample_dataset):
    python_scores = extract_module_scores(sample_dataset, "python")
    math_scores = extract_module_scores(sample_dataset, "math")

    assert python_scores["familiarity"][0] == sample_dataset[0]["modules"]["python"]["scores"]["mean_familiarity"]
    assert math_scores["familiarity"][0] == sample_dataset[0]["modules"]["math"]["scores"]["mean_familiarity"]

# test that the scatterplot creates a figure
def test_scatterplot():
    rng = np.random.default_rng(88)
    dataset = generate_dataset(rng, n_students=5)

    fig = plot_familiarity_ability(dataset, "python")

    assert fig is not None

    plt.close(fig)

# test that the histogram creates a figure
def test_histogram():
    rng = np.random.default_rng(88)
    dataset = generate_dataset(rng, n_students=5)

    fig = plot_composite_distribution(dataset, "math")

    assert fig is not None

    plt.close(fig)

# test that the recommendation boxplot creates a figure
def test_boxplot():
    rng = np.random.default_rng(88)
    dataset = generate_dataset(rng, n_students=50)

    fig = plot_recommendation_boxplot(dataset, "python")

    assert fig is not None

    plt.close(fig)