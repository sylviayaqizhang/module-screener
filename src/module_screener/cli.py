import argparse
from pathlib import Path

from module_screener.questionnaire import ask_questions
from module_screener.recommendations import recommendation_for
from module_screener.scoring import score_modules
from module_screener.storage import append_response


def main() -> None:
	parser = argparse.ArgumentParser(description="Collect module screener responses.")
	parser.add_argument(
		"--output",
		type=Path,
		default=Path("outputs") / "responses.json",
		help="JSON file for saved responses (default: outputs/responses.json)",
	)
	parser.add_argument(
		"--questions",
		type=Path,
		default=Path("data") / "questions.json",
		help="JSON file containing module examples (default: data/questions.json)",
	)
	args = parser.parse_args()

	print("=" * 48)
	print("WELCOME TO THE DTC MODULE SCREENER".center(48))
	print("=" * 48)
	print("Rate your familiarity and ability from 1 (lowest) to 4 (highest).")
	print("Your scores and recommendations will be saved.")
	print()

	answers = ask_questions(args.questions)
	scores = score_modules(answers)
	modules = {
		module_name: {
			"questions": module_answers,
			"scores": scores[module_name],
			"recommendation": recommendation_for(
				scores[module_name]["composite_score"]
			),
		}
		for module_name, module_answers in answers.items()
	}
	output_path = append_response({"modules": modules}, args.output)
	print(f"Thank you. Your responses were saved to {output_path}.")
