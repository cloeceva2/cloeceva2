"""
A light matplotlib intro
(with a sprinkling from
related NumPy/Pandas)
"""

from random import random

# SOOOOO much
# https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np
import numpy.typing as npt

#

def linegraph() -> None:
    """
    Example line plot
    """

    # produces [0, 0.1, 0.2 ... 4.8, 4.9]
    x: npt.NDArray[np.float64] = np.arange(0, 5, 0.1)

    # produces [sin(0), sin(0.1), ... sin(4.9)]
    y: npt.NDArray[np.float64] = np.sin(x)

    plt.plot(x, y)
    plt.show()


def scatterplot() -> None:
    """
    Example scatter plot
    """

    # 100 random x coordinates in [0, 1)
    x: list[float] = [random() for _ in range(100)]

    # corresponding y coordinates in (-1, 0]
    y: list[float] = [-i + 0.1 * random() for i in x]

    plt.scatter(x, y)

    plt.title('Relationship between x and y', fontsize=16, color='blue')
    plt.xlabel('x')  # title of the x axis
    plt.ylabel('y')  # title of the y axis

    plt.show()


def barchart() -> None:
    """
    Example bar chart
    """

    fave_beans: pd.Series = pd.Series([
        "dunkin", "onyx", "pavement",
        "pavement", "dunkin", "dunkin"
    ])

    fave_votes: pd.Series = fave_beans.value_counts()
    print(fave_votes)

    # plt.bar(fave_votes.index, fave_votes.values, color='coral')
    fave_votes.plot.bar(color='coral')

    plt.title('☕️ Votes')
    plt.xlabel('Roaster')
    plt.ylabel('Votes')

    plt.show()


def histogram() -> None:
    """
    Example histogram
    """

    # 1000 pts drawn from a normal
    # distribution centered on 42
    heights: npt.NDArray[np.float64] = np.random.normal(loc=42, size=1000)

    plt.hist(heights)

    plt.title("bell curve'ish")
    plt.show()


def main() -> None:
    """
    Kicking off the show!
    """

    linegraph()
    scatterplot()
    barchart()
    histogram()

if __name__ == "__main__":
    main()
