import matplotlib.pyplot as plt
import json
from module_screener.analysis.summary import extract_module_scores

# scatter plots for average familiarity against ability scores
def plot_familiarity_ability(dataset, module_name):
    scores = extract_module_scores(dataset, module_name)

    x = scores["familiarity"]
    y = scores["ability"]

    fig = plt.figure()
    plt.scatter(x, y)
    plt.axvline(x=2.5, linestyle="--", color="grey")
    plt.axhline(y=2.5, linestyle="--", color="grey")
    plt.xlim(1, 4)
    plt.ylim(1, 4)
    plt.xlabel("Mean familiarity")
    plt.ylabel("Mean ability")
    plt.title(f"{module_name.title()}: Familiarity vs Ability")

    return fig

# histogram for composite scores
def plot_composite_distribution(dataset, module_name):
    scores = extract_module_scores(dataset, module_name)

    composite = scores["composite"]

    fig = plt.figure()
    plt.hist(composite, bins=10, edgecolor="black")
    plt.xlabel("Composite score")
    plt.ylabel("Number of students")
    plt.title(f"{module_name.title()}: Composite Score Distribution")

    return fig

# generate a boxplot for summary scores in intro and advanced
def plot_recommendation_boxplot(dataset, module_name):
    intro_scores = []
    advanced_scores = []

    for student in dataset:
        module = student["modules"][module_name]
        score = module["scores"]["composite_score"]

        if module["recommendation"] == "intro":
            intro_scores.append(score)
        else:
            advanced_scores.append(score)

    fig = plt.figure()

    plt.boxplot(
        [intro_scores, advanced_scores],
        tick_labels=["Intro", "Advanced"]
    )

    plt.ylabel("Composite score")
    plt.title(f"{module_name.title()}: Scores by Recommended Level")

    return fig

if __name__ == "__main__":
    with open("data/demo_data.json", "r", encoding="utf-8") as file:
        dataset = json.load(file)

    plot_familiarity_ability(dataset, "python")
    plot_familiarity_ability(dataset, "math")

    plot_composite_distribution(dataset, "python")
    plot_composite_distribution(dataset, "math")

    plot_recommendation_boxplot(dataset, "python")
    plot_recommendation_boxplot(dataset, "math")

    plt.show()


