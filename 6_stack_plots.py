from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

days = [1, 2, 3, 4, 5, 6, 7, 8, 9]
labels = ["Developer 1", "Developer 2", "Developer 3"]

developers = [[1, 2, 3, 3, 4, 4, 4, 4, 5], [1, 1, 1, 1, 2, 2, 2, 3, 4], [1, 1, 1, 2, 2, 2, 3, 3, 3]]

plt.stackplot(days, *developers, labels=labels)

plt.legend(loc="upper left")
plt.title("Developers contributions")
plt.xlabel("Days")
plt.ylabel("Contributions")

plt.tight_layout()
plt.savefig("img/stack_plots.png")
plt.show()
