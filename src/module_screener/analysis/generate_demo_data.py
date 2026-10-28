import numpy as np

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

# function to generate a complete student record with python and math modules
def generate_student(student_id, rng):
    student = {
        "id": f"{student_id:03d}",
        "modules": {}
    }

    # generate responses for python questions and store in student dictionary
    python_questions = generate_module_responses(rng)
    student["modules"]["python"] = {"questions": python_questions}

    # generate responses for math questions and store in student dictionary
    math_questions = generate_module_responses(rng)
    student["modules"]["math"] = {"questions": math_questions}

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

# generate dataset
# only run the following code when the file is run directly
if __name__ == "__main__":
    rng = np.random.default_rng(88)
    dataset = generate_dataset(rng)

    print(len(dataset))
    print(dataset[0])
