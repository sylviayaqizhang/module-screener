import json

from module_screener.questionnaire import ask_questions


def test_ask_questions_displays_examples_and_retries_invalid_scores(tmp_path):
	question_file = tmp_path / "questions.json"
	question_file.write_text(
		json.dumps(
			{
				"modules": {
					"programming": {
						"questions": {"Q1": {"example": "print(2 + 2)"}}
					},
					"math": {
						"questions": {"Q1": {"example": "Solve 3x = 12"}}
					},
				}
			}
		),
		encoding="utf-8",
	)
	answers = iter(["", "5", "3", "2", "", "0", "4", "1"])
	displayed = []
	prompts = []

	def answer_prompt(prompt):
		prompts.append(prompt)
		return next(answers)

	responses = ask_questions(
		question_file,
		input_fn=answer_prompt,
		output_fn=displayed.append,
	)

	assert responses == {
		"programming": {"Q1": {"familiarity": 3, "ability": 2}},
		"math": {"Q1": {"familiarity": 4, "ability": 1}},
	}
	assert "print(2 + 2)" in displayed
	assert "Solve 3x = 12" in displayed
	assert "PROGRAMMING SCREENING".center(60) in displayed
	assert "MATH SCREENING".center(60) in displayed
	assert any("Q1" in section and "-" * 60 in section for section in displayed)
	assert displayed.count("Please enter a whole number from 1 to 4.") == 2
	assert prompts[0] == "Press enter to continue to the Programming screening"
	assert "Press enter to continue to the Math screening" in prompts
