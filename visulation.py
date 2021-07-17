import matplotlib.pyplot as plt
import numpy as np

def graph(x, y):
    fig, ax = plt.subplots()
    x_values = np.arange(0, x)

    plt.title("Game of life")
    plt.xlabel("Runs")
    plt.ylabel("Remaining cells in %")

    plt.axis([0, x, 0, 100])
    plt.xticks(np.arange(0, x + 1, 1.0))
    for i, j in zip(x_values, y):
        ax.annotate(str(round(j)), xy=(i, j))

    plt.plot(x_values, y, "-o")
    plt.show()