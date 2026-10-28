import numpy as np

from module_screener.analysis.generate_demo_data import (
    generate_module_responses,
    generate_student,
    generate_dataset,
)

# test if the number of questions is correct, 5 questions
def test_question_count():
    rng = np.random.default_rng(88)
    questions = generate_module_responses(rng)

    assert  len(questions) == 5

# test if the responses are valid, integers between 1-4
def test_valid_rating():
    rng = np.random.default_rng(88)
    questions = generate_module_responses(rng)
    familiarity = questions["Q1"]["familiarity"]

    assert 1 <= familiarity <= 4

# test if student profiles have valid components
def test_student_structure():
    rng = np.random.default_rng(88)
    student = generate_student(1, rng)

    # check if student id is in right format
    assert student["id"] == "001"

    # check that both modules exist
    assert "python" in student["modules"]
    assert "math" in student["modules"]

# test if the dataset generates 50 students
def test_dataset_size():
    rng = np.random.default_rng(88)
    dataset = generate_dataset(rng)

    assert len(dataset) == 50

# test if student id is valid and unique
def test_student_id():
    rng = np.random.default_rng(88)
    dataset = generate_dataset(rng)

    ids = []
    for student in dataset:
        ids.append(student["id"])

        # check if the id number is 3 digit
        assert len(student["id"]) == 3
        assert student["id"].isdigit()

    # check if id is unique
    assert len(ids) == len(set(ids))

