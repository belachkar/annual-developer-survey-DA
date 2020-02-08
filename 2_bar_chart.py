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

# Setting the plots
plt.bar(x_indexes - bar_width, py_dev_y, width=bar_width, color="#008fd5", label="Python")
plt.bar(x_indexes, js_dev_y, width=bar_width, color="#e5ae38", label="JS")
plt.bar(x_indexes + bar_width, dev_y, width=bar_width, color="#555555", label="All Devs")

# Set the x labels to ages_x insead of x_indexes used for shifting tha bars
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
