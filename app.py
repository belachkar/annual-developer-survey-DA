from matplotlib import pyplot as plt

# Turn on xkcd <https://xkcd.com/>_ sketch-style drawing mode.
# plt.xkcd()

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Setting the plots
plt.plot(ages_x, py_dev_y, color="#5a7d9a", linewidth=2, label="Python")
plt.plot(ages_x, js_dev_y, color="#adad3b", linewidth=2, label="JS")
plt.plot(ages_x, dev_y, color="#444444", linestyle="--", marker=".", label="All Devs")

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

# Print available styles
# print(plt.style.available)

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
