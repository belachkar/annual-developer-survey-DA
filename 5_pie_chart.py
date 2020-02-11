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

languages, popularity = zip(*lng_counter.most_common(5))

# Offsetting the wedges, Python in this example by 10% of the radius
explode = [0, 0, 0, 0.1, 0]

plt.pie(
    popularity,
    labels=languages,
    explode=explode,
    shadow=True,
    autopct="%1.1f%%",  # Auto implemanting percentages
    wedgeprops={"edgecolor": "black"},
)

plt.title("Pie chart")
plt.tight_layout()

plt.savefig("img/pie_chart.png")
plt.show()
