import pytest

from module_screener.scoring import score_modules


def test_score_modules_calculates_means_and_composite_per_module():
	answers = {
		"programming": {
			"Q1": {"familiarity": 4, "ability": 2},
			"Q2": {"familiarity": 2, "ability": 4},
		},
		"math": {"Q1": {"familiarity": 3, "ability": 1}},
	}

	assert score_modules(answers) == {
		"programming": {
			"mean_familiarity": 3.0,
			"mean_ability": 3.0,
			"composite_score": 3.0,
		},
		"math": {
			"mean_familiarity": 3.0,
			"mean_ability": 1.0,
			"composite_score": 2.0,
		},
	}


def test_score_modules_rejects_modules_without_questions():
	with pytest.raises(ValueError, match="no answered questions"):
		score_modules({"programming": {}})
