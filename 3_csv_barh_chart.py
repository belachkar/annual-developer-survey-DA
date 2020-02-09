import csv
from collections import Counter
from matplotlib import pyplot as plt


with open("data/data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    languages_counter = Counter()

    for row in csv_reader:
        languages_counter.update(row["LanguagesWorkedWith"].split(";"))

languages, popularity = zip(*languages_counter.most_common(15))
languages, popularity = list(languages), list(popularity)

# Reversing values to have bigger values at top
languages.reverse()
popularity.reverse()

# Select a style
plt.style.use("fivethirtyeight")

# Horizontal bar chart
plt.barh(languages, popularity)

plt.legend()

plt.title("Most Popular Languages")
# plt.ylabel("Progamming Languages")
plt.xlabel("Popularity")

plt.tight_layout()

plt.savefig("img/barh_chart.png")
plt.show()
