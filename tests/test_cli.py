import json

from module_screener.cli import main


def test_main_saves_scored_module_responses(tmp_path, monkeypatch, capsys):
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
	output_file = tmp_path / "responses.json"
	answers = iter(["", "4", "3", "", "2", "1"])
	monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))
	monkeypatch.setattr(
		"sys.argv",
		[
			"module-screener",
			"--questions",
			str(question_file),
			"--output",
			str(output_file),
		],
	)

	main()

	with output_file.open(encoding="utf-8") as json_file:
		record = json.load(json_file)[0]

	assert record["id"] == "001"
	assert record["modules"]["programming"] == {
		"questions": {"Q1": {"familiarity": 4, "ability": 3}},
		"scores": {
			"mean_familiarity": 4.0,
			"mean_ability": 3.0,
			"composite_score": 3.5,
		},
		"recommendation": "advanced",
	}
	assert record["modules"]["math"]["recommendation"] == "intro"
	output = capsys.readouterr().out
	assert "print(2 + 2)" in output
	assert "MODULE RECOMMENDATIONS" in output
	assert "PROGRAMMING" in output
	assert "MATH" in output
	assert ">>> ADVANCED <<<" in output
	assert ">>> INTRO <<<" in output
	assert "composite score" not in output.lower()