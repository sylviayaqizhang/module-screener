# module-screener

The module screener is a prototype command line interface program that assesses the user's abilities in two modules, Programming and Math, and recommends a course to the user based on their confidence. The program takes two values for each question: a familiarity score and an ability score. The questions are designed to show examples of concepts so the user knows exactly what is being tested. The program has two parts: the actual CLI part, and a data analysis portion. For the data analysis portion, pseudodata is generated on the spot to give an idea for what kinds of statistics will be available from the data.

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


## Cohort Analysis for Demonstration

From the repository root, with the virtual environment activated:

### 1. Generate synthetic data (50 students)
```bash
python -m module_screener.analysis.generate_demo_data
```

### 2. View summary statistics
```bash
python -m module_screener.analysis.summary
```

### 3. View visualisations
```bash
python -m module_screener.analysis.visualisation
```

# Run without installing the package

Use `PYTHONPATH=src` before each command:

```bash
PYTHONPATH=src python -m module_screener.analysis.generate_demo_data
PYTHONPATH=src python -m module_screener.analysis.summary
PYTHONPATH=src python -m module_screener.analysis.visualisation
```

*All data and recommendations are synthetic and for demonstration purposes only.*
