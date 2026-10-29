ADVANCED_SCORE_THRESHOLD = 2.5


def recommendation_for(composite_score: float) -> str:
	"""Recommend advanced study above the threshold, intro otherwise."""
	if composite_score > ADVANCED_SCORE_THRESHOLD:
		return "advanced"
	return "intro"
