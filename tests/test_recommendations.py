from module_screener.recommendations import recommendation_for


def test_recommendation_uses_strict_greater_than_threshold():
	assert recommendation_for(2.5) == "intro"
	assert recommendation_for(2.51) == "advanced"
