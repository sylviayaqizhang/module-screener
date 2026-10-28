import numpy as np
import json
from pathlib import Path
import statistics

# function to generate question dictionary storing familiarity and ability scores
def generate_module_responses(rng, n_questions=5):
    questions = {}

    for i in range(1, n_questions + 1):
        question_id = f"Q{i}"

        # Generate familiarity and ability scores

        familiarity_score = int(rng.integers(1, 5))
        ability_score = int(rng.integers(1, 5))

        # Store them inside questions[question_id]

        questions[question_id] = {"familiarity": familiarity_score,
                                  "ability": ability_score}

    return questions


# function to calculate composite scores
def calculate_module_scores(questions):
    # extract familiarity and ability scores
    familiarity_scores = [
        response["familiarity"]
        for response in questions.values()
    ]

    ability_scores = [
        response["ability"]
        for response in questions.values()
    ]

    # calculate mean familiarity and mean ability scores
    mean_familiarity = statistics.mean(familiarity_scores)
    mean_ability = statistics.mean(ability_scores)

    # average two scores to get the composite score
    composite_score = (mean_familiarity + mean_ability) / 2

    return {
        "mean_familiarity": mean_familiarity,
        "mean_ability": mean_ability,
        "composite_score": composite_score
    }

# function to recommend module levels based on composite scores
def recommend_level(composite_score):
    if composite_score >= 2.5:
        return "advanced"
    else:
        return "intro"

# function to generate a complete student record with python and math modules
def generate_student(student_id, rng):
    student = {
        "id": f"{student_id:03d}",
        "modules": {}
    }

    # generate python responses
    python_questions = generate_module_responses(rng)
    # generate python scores
    python_scores = calculate_module_scores(python_questions)
    # generate python recommendation
    python_recommendation = recommend_level(python_scores["composite_score"])
    # store python results
    student["modules"]["python"] = {
        "questions": python_questions,
        "scores": python_scores,
        "recommendation": python_recommendation
    }

    # generate maths responses
    math_questions = generate_module_responses(rng)
    # calculate maths scores
    math_scores = calculate_module_scores(math_questions)
    # generate maths recommendation
    math_recommendation = recommend_level(math_scores["composite_score"])
    # store maths results
    student["modules"]["math"] = {
        "questions": math_questions,
        "scores": math_scores,
        "recommendation": math_recommendation
    }





    return student


# function to generate full student dataset
def generate_dataset(rng, n_students=50):
    students = []

    for i in range(1, n_students + 1):
        # generate one student using i and rng
        student = generate_student(i, rng)

        # add that student to the students list
        students.append(student)

    return students

# save dataset to a json file
def save_dataset(dataset, filepath):
    filepath = Path(filepath)

    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(dataset, file, indent=2)


# generate dataset
# only run the following code when the file is run directly
if __name__ == "__main__":
    rng = np.random.default_rng(88)
    dataset = generate_dataset(rng)

    output_path = Path("data/demo_data.json")
    save_dataset(dataset, output_path)

    print(len(dataset))
    print(dataset[0])
    print(f"Saved {len(dataset)} students to {output_path}")