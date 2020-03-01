import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("data/ages.csv")

ages = data["Age"]
ids = data["Responder_id"]

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, edgecolor="black")

median_age = pd.DataFrame.median(ages)
color = "#fc4f30"
plt.axvline(median_age, color=color, label="Median Age")

plt.legend()
plt.title("Ages of Respondents")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")

plt.tight_layout()
plt.show()
