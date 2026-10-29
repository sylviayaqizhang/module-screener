# module-screener

## Run the screener program

Create the virtual environment and install the project with its test tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

With the environment active, start the interactive screener:

```bash
module-screener
```

Run the test suite with `pytest`. When you're finished, leave the environment with
`deactivate`.

The program reads questions from `data/questions.json`, asks for familiarity and
ability ratings from 1 to 4, calculates scores per module, and appends response, composite score, and module recommendation to `outputs/responses.json`. To use different question or
output files, pass `--questions` and `--output`:

```bash
module-screener --questions data/questions.json --output outputs/responses.json
```

You can also run it from the source tree without installing:

```bash
PYTHONPATH=src python -m module_screener
```