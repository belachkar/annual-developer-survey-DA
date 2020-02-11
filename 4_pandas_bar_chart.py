from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd


# Selecting a style
plt.style.use("fivethirtyeight")

data = pd.read_csv("data/data.csv")

ids = data["Responder_id"]
lng_rows = data["LanguagesWorkedWith"]

lng_counter = Counter()

for lng_row in lng_rows:
    lng_counter.update(lng_row.split(";"))

languages, popularity = zip(*lng_counter.most_common(15))
languages, popularity = list(languages), list(popularity)

languages.reverse()
popularity.reverse()

# Horizontal bar chart
plt.barh(languages, popularity)

plt.legend()
plt.title("Most Popular Languages")
plt.xlabel("Popularity")

plt.tight_layout()
# plt.savefig("img/barh_chart.png")
plt.show()
