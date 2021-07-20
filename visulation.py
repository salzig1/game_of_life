import matplotlib.pyplot as plt
import numpy as np

def graph(x1, y1, x2, y2):
    fig, (ax1, ax2) = plt.subplots(2, 1)

    x2_values = np.arange(0, x2)
    ax2.set_title("Cell developement")
    ax2.set_xlabel("Generations")
    ax2.set_ylabel("Amount cells")

    x1_values = np.arange(0, x1)
    ax1.set_title("Remaining cells")
    ax1.set_xlabel("Runs")
    ax1.set_ylabel("Remaining cells in %")
    ax1.axis([0, x1, 0, 100])
    ax1.set_xticks(np.arange(0, x1 + 1, 1.0))
    for i, j in zip(x1_values, y1):
        ax1.annotate(str(round(j)), xy=(i, j))

    plt.subplots_adjust(hspace=0.5)
    ax1.plot(x1_values, y1, "-o")
    ax2.plot(x2_values, y2, "-")
    plt.show()