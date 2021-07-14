import matplotlib.pyplot as plt
import numpy as np

def graph(x, y):
    fig, ax = plt.subplots()
    x = np.arange(0, x)

    plt.plot(x, y)
    plt.show()