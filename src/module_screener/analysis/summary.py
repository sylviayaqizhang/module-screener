import json
import statistics

# extract scores
def extract_module_scores(dataset, module_name):
    familiarity = []
    ability = []
    composite = []

    for student in dataset:
        scores = student["modules"][module_name]["scores"]

        familiarity.append(scores["mean_familiarity"])
        ability.append(scores["mean_ability"])
        composite.append(scores["composite_score"])

    return {
        "familiarity": familiarity,
        "ability": ability,
        "composite": composite
    }

# calculate summary statistics
def summarise_scores(values):
    return {
        "n": len(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "sd": statistics.stdev(values),
        "min": min(values),
        "max": max(values)
    }

# summarise module scores
def summarise_module(dataset, module_name):
    scores = extract_module_scores(dataset, module_name)

    return {
        "familiarity": summarise_scores(scores["familiarity"]),
        "ability": summarise_scores(scores["ability"]),
        "composite": summarise_scores(scores["composite"])
    }

# print summary statistics in a readable table
def print_summary(summary, module_name):
    columns = ["n", "mean", "median", "sd", "min", "max"]

    print(f"\n{module_name.upper()} SUMMARY")
    print(f"{'Measure':<15}" + "".join(f"{col.title():>9}" for col in columns))
    print("-" * 69)

    for measure, stats in summary.items():
        values = "".join(
            f"{stats[col]:>9.0f}" if col == "n" else f"{stats[col]:>9.2f}"
            for col in columns
        )
        print(f"{measure.capitalize():<15}{values}")

if __name__ == "__main__":
    with open("data/demo_data.json", "r", encoding="utf-8") as file:
        dataset = json.load(file)

    python_summary = summarise_module(dataset, "python")
    math_summary = summarise_module(dataset, "math")

    print_summary(python_summary, "python")
    print_summary(math_summary, "math")
