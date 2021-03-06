import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("data/developers.csv")

ages = data["Age"]
dev_salaries = data["All_Devs"]
py_salaries = data["Python"]
js_salaries = data["JavaScript"]

median = pd.DataFrame.median(dev_salaries)

plt.plot(ages, py_salaries, label="Python")
plt.plot(ages, dev_salaries, label="All Devs", linestyle="--")

plt.fill_between(
    ages,
    py_salaries,
    dev_salaries,
    where=(py_salaries > dev_salaries),
    interpolate=True,
    alpha=0.2,
    label="Above Avg",
)

plt.fill_between(
    ages,
    py_salaries,
    dev_salaries,
    where=(py_salaries <= dev_salaries),
    interpolate=True,
    alpha=0.2,
    label="Below Avg",
)

plt.legend()
plt.title("Median salary (USD) by Age")
plt.xlabel("Ages")

plt.tight_layout()
plt.show()
