import json

from module_screener.storage import append_response


def test_append_response_adds_records_to_json_array(tmp_path):
	output_path = tmp_path / "nested" / "responses.json"
	first_response = {"modules": {"programming": {"recommendation": "advanced"}}}
	second_response = {"modules": {"math": {"recommendation": "intro"}}}

	append_response(first_response, output_path)
	append_response(second_response, output_path)

	with output_path.open(encoding="utf-8") as json_file:
		rows = json.load(json_file)

	assert len(rows) == 2
	assert rows[0]["id"] == "001"
	assert rows[0]["modules"]["programming"]["recommendation"] == "advanced"
	assert rows[1]["id"] == "002"
	assert rows[1]["modules"]["math"]["recommendation"] == "intro"
