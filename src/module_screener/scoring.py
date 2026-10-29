from collections.abc import Mapping


def score_modules(
	responses: Mapping[str, Mapping[str, Mapping[str, int]]],
) -> dict[str, dict[str, float]]:
	"""Calculate mean familiarity, mean ability, and composite per module."""
	module_scores = {}
	for module_name, questions in responses.items():
		if not questions:
			raise ValueError(f"Module {module_name!r} has no answered questions.")

		familiarity_values = [
			answer["familiarity"] for answer in questions.values()
		]
		ability_values = [answer["ability"] for answer in questions.values()]
		mean_familiarity = sum(familiarity_values) / len(familiarity_values)
		mean_ability = sum(ability_values) / len(ability_values)
		module_scores[module_name] = {
			"mean_familiarity": round(mean_familiarity, 2),
			"mean_ability": round(mean_ability, 2),
			"composite_score": round((mean_familiarity + mean_ability) / 2, 2),
		}
	return module_scores
