import matplotlib.pyplot as plt
import json
from module_screener.analysis.summary import extract_module_scores

# scatter plots for average familiarity against ability scores
def plot_familiarity_ability(dataset, module_name, ax=None):
    scores = extract_module_scores(dataset, module_name)

    x = scores["familiarity"]
    y = scores["ability"]

    if ax is None:
        _, ax = plt.subplots()
    ax.scatter(x, y)
    ax.axvline(x=2.5, linestyle="--", color="grey")
    ax.axhline(y=2.5, linestyle="--", color="grey")
    ax.set_xlim(1, 4)
    ax.set_ylim(1, 4)
    ax.set_xlabel("Mean familiarity")
    ax.set_ylabel("Mean ability")
    ax.set_title(f"{module_name.title()}: Familiarity vs Ability")

    return ax.figure

# histogram for composite scores
def plot_composite_distribution(dataset, module_name, ax=None):
    scores = extract_module_scores(dataset, module_name)

    composite = scores["composite"]

    if ax is None:
        _, ax = plt.subplots()
    ax.hist(composite, bins=10, edgecolor="black")
    ax.set_xlabel("Composite score")
    ax.set_ylabel("Number of students")
    ax.set_title(f"{module_name.title()}: Composite Score Distribution")

    return ax.figure

# generate a boxplot for summary scores in intro and advanced
def plot_recommendation_boxplot(dataset, module_name, ax=None):
    intro_scores = []
    advanced_scores = []

    for student in dataset:
        module = student["modules"][module_name]
        score = module["scores"]["composite_score"]

        if module["recommendation"] == "intro":
            intro_scores.append(score)
        else:
            advanced_scores.append(score)

    if ax is None:
        _, ax = plt.subplots()

    ax.boxplot(
        [intro_scores, advanced_scores],
        tick_labels=["Intro", "Advanced"]
    )

    ax.set_ylabel("Composite score")
    ax.set_title(f"{module_name.title()}: Scores by Recommended Level")

    return ax.figure


def plot_all_figures(dataset):
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))

    for column, module_name in enumerate(("python", "math")):
        plot_familiarity_ability(dataset, module_name, ax=axes[0, column])
        plot_composite_distribution(dataset, module_name, ax=axes[1, column])
        plot_recommendation_boxplot(dataset, module_name, ax=axes[2, column])

    fig.suptitle("Module Screening Overview", fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return fig

if __name__ == "__main__":
    with open("data/demo_data.json", "r", encoding="utf-8") as file:
        dataset = json.load(file)

    plot_all_figures(dataset)
    plt.show()


