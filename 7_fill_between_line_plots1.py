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
    ages, py_salaries, median, where=(py_salaries > median), interpolate=True, alpha=0.2
)

plt.fill_between(
    ages, py_salaries, median, where=(py_salaries <= median), interpolate=True, alpha=0.2
)

plt.legend()
plt.title("Median salary (USD) by Age")
plt.xlabel("Ages")

plt.tight_layout()
plt.show()
