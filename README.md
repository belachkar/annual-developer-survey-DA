# Annual Developer Survey - Data Analysis  <!-- omit in toc -->

## Table Of Contents <!-- omit in toc -->

- [Dependecies](#dependecies)
- [Plot chart](#plot-chart)
- [Bar chart](#bar-chart)
- [Horizontal bar chart](#horizontal-bar-chart)
  - [Using csv package](#using-csv-package)
  - [Using pandas package](#using-pandas-package)
- [Pie chart](#pie-chart)
- [Useful codes](#useful-codes)
  - [Printing available styles](#printing-available-styles)
  - [Turning on XKCD effect for rendering an image](#turning-on-xkcd-effect-for-rendering-an-image)
- [References](#references)

## Dependecies

| Name           | Description                                                                                                                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **matplotlib** | A plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+. |
| **NumPy**      | A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.                                         |

## Plot chart

```python
from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Setting the plots
plt.plot(ages_x, py_dev_y, color="#008fd5", linewidth=2, label="Python")
plt.plot(ages_x, js_dev_y, color="#e5ae38", linewidth=2, label="JS")
plt.plot(ages_x, dev_y, color="#444444", linestyle="--", marker=".", label="All Devs")

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# Select a style
plt.style.use("fivethirtyeight")

# Setting the grid
plt.grid(True)

# Setting the legends
plt.legend()

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Saving the file automatically
plt.savefig("img/plot.png")

# Display a figure.
plt.show()
```

![plot-chart]

## Bar chart

```python
from matplotlib import pyplot as plt
import numpy as np

# Select a style
plt.style.use("fivethirtyeight")

bar_width = 0.25
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Getting a list of indexes, used to get the bars side by side
x_indexes = np.arange(len(ages_x))

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Setting the bars, using bar_width offsets to get the bars side by side
plt.bar(x_indexes - bar_width, py_dev_y, width=bar_width, color="#008fd5", label="Python")
plt.bar(x_indexes, js_dev_y, width=bar_width, color="#e5ae38", label="JS")
plt.bar(x_indexes + bar_width, dev_y, width=bar_width, color="#555555", label="All Devs")

# Set the x labels to ages_x insead of x_indexes used for shifting the bars
plt.xticks(ticks=x_indexes, labels=ages_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# Setting the grid
plt.grid(True)

# Setting the legends
plt.legend()

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Saving the file automatically
plt.savefig("img/bar_chart.png")

# Display a figure.
plt.show()
```

![bar-chart]

## Horizontal bar chart

### Using csv package

```python
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

# Reversing values to get bigger values at top
languages.reverse()
popularity.reverse()

# Select a style
plt.style.use("fivethirtyeight")

# Horizontal bar chart
plt.barh(languages, popularity)

plt.legend()

plt.title("Most Popular Languages")
plt.xlabel("Popularity")

plt.tight_layout()

plt.savefig("img/barh_chart.png")
plt.show()
```

### Using pandas package

```python
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
```

![Horizontal Bar Chart]

## Pie chart

```python
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
```

![Pie chart]

## Useful codes

### Printing available styles

```python
from matplotlib import pyplot as plt

print(plt.style.available)

# Output:
['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']
```

### Turning on XKCD effect for rendering an image

Turning on xkcd <https://xkcd.com/> _sketch-style drawing mode_.

```python
from matplotlib import pyplot as plt

plt.xkcd()
```

![xkcd_plot]

## References

- Datasets from [stackoverflow dataset](https://insights.stackoverflow.com/survey)
- Tutorial videos [Corey Schafer YT channel]

<!-- Links -->
[xkcd_plot]: https://i.ibb.co/s2swsDy/plot.png "XKCD Plot"
[plot-chart]: https://i.ibb.co/4WNks6Z/plot-chart.png "Plot chart"
[bar-chart]: https://i.ibb.co/Fm4mKX5/bar-chart.png "Bar chart"
[stackoverflow dataset]: https://insights.stackoverflow.com/survey "Stackoverflow dataset"
[Corey Schafer YT channel]: https://www.youtube.com/watch?v=nKxLfUrkLE8 "Corey Schafer"
[Horizontal Bar Chart]: https://i.ibb.co/TqmL02B/barh-chart.png "Horizontal Bar Chart"
[Pie chart]: https://i.ibb.co/w7zywD2/pie-chart.png "Pie chart"
