import json
from collections.abc import Callable
from pathlib import Path


RATING_PROMPTS = (
	("familiarity", "How familiar are you with the ideas in this example?"),
	("ability", "How able do you feel to solve a similar problem?"),
)


class QuestionnaireExit(Exception):
	"""Raised when the user chooses to leave the questionnaire."""


def _read_input(prompt: str, input_fn: Callable[[str], str]) -> str:
	answer = input_fn(prompt).strip()
	if answer.lower() == "exit":
		raise QuestionnaireExit
	return answer


def ask_questions(
	question_file: str | Path = Path("data") / "questions.json",
	input_fn: Callable[[str], str] | None = None,
	output_fn: Callable[[str], None] | None = None,
) -> dict[str, dict[str, dict[str, int]]]:
	"""Display questions and collect familiarity and ability ratings from 1 to 4."""
	if input_fn is None:
		input_fn = input
	if output_fn is None:
		output_fn = print

	with Path(question_file).open(encoding="utf-8") as json_file:
		question_data = json.load(json_file)

	responses = {}
	for module_name, module_data in question_data["modules"].items():
		_read_input(
			f"Press enter to continue to the {module_name.title()} screening",
			input_fn,
		)
		output_fn("\n" + "=" * 60)
		output_fn(f"{module_name.upper()} SCREENING".center(60))
		output_fn("=" * 60)
		responses[module_name] = {}
		for question_id, question_data in module_data["questions"].items():
			output_fn(f"\n{'-' * 60}\n{question_id} \n{'-' * 60}")
			output_fn(question_data["example"])
			output_fn("-" * 60)
			responses[module_name][question_id] = {}
			for rating, prompt in RATING_PROMPTS:
				while True:
					answer = _read_input(f"{prompt} (1-4)\n> ", input_fn)
					try:
						score = int(answer)
					except ValueError:
						score = 0
					if 1 <= score <= 4:
						responses[module_name][question_id][rating] = score
						break
					output_fn("Please enter a whole number from 1 to 4.")
	return responses
