"""
A little work on correlation
"""

from random import random

import sympy as sp # type: ignore
import matplotlib.pyplot as plt

import pandas as pd

#

def display_latex(latex: str) -> None:
    """
    Visually displays LaTeX
    via matplotlib
    """

    _, ax = plt.subplots()

    # Hide axes
    ax.axis('off')

    # Display equation using LaTeX
    plt.text(
        0.5, 0.5,
        f'${ latex }$',
        fontsize=20, ha='center', va='center'
    )

    plt.show()


def for_fun() -> None:
    """Just showing some SymPy"""

    x, y = sp.symbols('x, y')
    eq = sp.Eq(y, x ** 2)

    display_latex(sp.latex(eq))
    display_latex(sp.latex(eq.subs([(x, 7)])))

    str_expr = "x**2 + 3*x - 1/2"
    expr = sp.sympify(str_expr)
    display_latex(sp.latex(expr))

    for e in sp.solveset(sp.Eq(0, expr)):
        display_latex(sp.latex(e))


def pearson() -> None:
    """LaTeX viz of Pearson correlation"""

    display_latex((
        'r_{xy} = \\frac{\\sum_{i=1}^{n}(x_i-\\bar{x})(y_i-\\bar{y})}'
        '{ \\sqrt{\\sum_{i=1}^{n}(x_i-\\bar{x})^2}'
        '\\sqrt{\\sum_{i=1}^{n}(y_i-\\bar{y})^2} }'
    ))


def _correlation(x: list[float], y: list[float]) -> None:
    """
    Utility to display x/y
    along with correlation
    """

    plt.scatter(x, y)

    plt.title('Corr: ???', fontsize=16, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

    #

    s1: pd.Series = pd.Series(x)
    s2: pd.Series = pd.Series(y)

    plt.scatter(x, y)
    plt.title(f'Corr: { s1.corr(s2) }', fontsize=16, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def produce_correlation(is_pos: bool, noise: float) -> None:
    """
    Correlation example

    Parameters
    ==========
    is_pos: bool
        True if desired a positive
        correlation

    noise: float
        noise radius to add to 
        each point
    """

    # 100 random x coordinates in [0, 1)
    x: list[float] = [random() for _ in range(100)]

    # corresponding y coordinates
    mult: float = 1 if is_pos else -1
    y: list[float] = [mult * i + noise * random() for i in x]

    _correlation(x, y)


def no_correlation() -> None:
    """No correlation example"""

    # 100 random x coordinates in [0, 1)
    x: list[float] = [random() for _ in range(100)]

    # corresponding y coordinates
    y: list[float] = [random() for _ in x]

    _correlation(x, y)


def main() -> None:
    """Let's go!!"""

    for_fun()
    pearson()
    produce_correlation(True, 0.1)
    produce_correlation(False, 0.25)
    produce_correlation(True, 1.5)
    produce_correlation(False, 0.9)
    produce_correlation(False, 0.01)
    produce_correlation(True, 3)
    no_correlation()


if __name__ == "__main__":
    main()
