import json
from collections.abc import Mapping
from pathlib import Path


def append_response(
	response: Mapping[str, object],
	output_path: str | Path = Path("outputs") / "responses.json",
) -> Path:
	"""Append one completed questionnaire to a JSON array."""
	path = Path(output_path)
	path.parent.mkdir(parents=True, exist_ok=True)
	if path.exists() and path.stat().st_size:
		with path.open(encoding="utf-8") as json_file:
			responses = json.load(json_file)
	else:
		responses = []
	if not isinstance(responses, list):
		raise ValueError("The response file must contain a JSON array.")

	record = {**response, "id": f"{len(responses) + 1:03d}"}
	responses.append(record)
	with path.open("w", encoding="utf-8") as json_file:
		json.dump(responses, json_file, indent=2)
		json_file.write("\n")

	return path
