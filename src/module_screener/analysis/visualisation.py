import matplotlib.pyplot as plt
import json
from module_screener.analysis.summary import extract_module_scores

# scatter plots for average familiarity against ability scores
def plot_familiarity_ability(dataset, module_name):
    scores = extract_module_scores(dataset, module_name)

    x = scores["familiarity"]
    y = scores["ability"]

    plt.scatter(x, y)
    plt.xlabel("Mean familiarity")
    plt.ylabel("Mean ability")
    plt.title(f"{module_name.title()}: Familiarity vs Ability")
    plt.show()

# histogram for composite scores
def plot_composite_distribution(dataset, module_name):
    scores = extract_module_scores(dataset, module_name)

    composite = scores["composite"]

    plt.figure()
    plt.hist(composite, bins=10, edgecolor="black")
    plt.xlabel("Composite score")
    plt.ylabel("Number of students")
    plt.title(f"{module_name.title()}: Composite Score Distribution")
    plt.show()

if __name__ == "__main__":
    with open("data/demo_data.json", "r", encoding="utf-8") as file:
        dataset = json.load(file)

    plot_familiarity_ability(dataset, "python")
    plot_familiarity_ability(dataset, "math")

    plot_composite_distribution(dataset, "python")
    plot_composite_distribution(dataset, "math")
