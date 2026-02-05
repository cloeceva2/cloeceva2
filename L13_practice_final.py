"""
Some practice related to data & functions
"""

from typing import Callable, TypeVar

import unittest

import numpy as np

##################################################
# 1. Normalizing data
##################################################

# When analyzing data, we often need to
# have our data in comparable scales
# so that the magnitude of one doesn't
# dwarf the other (think # bedrooms vs
# cost in $'s of a house).
#
# One comment approach is to scale all
# dimensions of the data points into
# a common range (e.g., [0, 1]) using
# the following transformation:

# x_i = (x_i - x_min) / (x_max - x_min)

# SO, implement the following function
# so that it passes the supplied tests,
# ideally using our great new Python
# superpowers :)

def normalize(vals: list[float]) -> list[float]:
    """
    Normalizes the supplied data
    points into [0, 1]

    Parameters
    ==========
    vals: list[float]
        numbers to normalize

    Returns
    =======
    list[float]
        normalized values

    Raises
    ======
    ValueError
        fewer than two distinct
        values are supplied
    """

    if len(set(vals)) < 2:
        raise ValueError

    x_max: float = max(vals)
    x_min: float = min(vals)

    nf: Callable[[float], float] = lambda x_i: (x_i - x_min) / (x_max - x_min)

    return [nf(x) for x in vals]


##################################################
# 2. Custom sorting
##################################################

# Commonly we have data we'd like to sort
# based upon custom metrics; for example,
# housing applications using different
# priorities (cough, HW1).

# SO, implement the following function
# that takes a list of items, as well
# as a function that provides an
# evaluation of a single item, and then
# produces a list of the top-k items (default
# of k=3).
#
# To help...
# * numpy provides argsort, which gives 
#   you a sorting of the indices of a 
#   sorted structure.
# * you also have a suggested sequence
#   of steps below

T = TypeVar('T')

def top_k(items: list[T], eval_f: Callable[[T], float], k: int = 3) -> list[T]:
    """
    Get the top-k elements in a supplied
    list according to a custom eval
    function.

    Parameters
    ==========
    items: list[T]
        items to evaluate

    eval_f: Callable[[T], float]
        evaluation function

    k: int
        how many items to return

    Returns
    =======
    list[T]
        top-k items ordered by the
        evaluation function

    Raises
    ======
    ValueError
        Too few items supplied for k
    """

    # note: to order descending with argsort, since it is ascending, either...
    # - negate the evaluation function result
    #   (so biggest eval becomes smallest)
    # - iterate through indexes in reverse: list[::-1]

    # 1. ensure there are enough items
    if len(items) < k:
        raise ValueError

    # 2. rate each item
    ratings: list[float] = [eval_f(i) for i in items]

    # 3. argsort according to ratings
    ordered_indexes: list[int] = np.argsort(np.array(ratings)).tolist()

    # 4. cross-reference the indices in order
    #    with the original items to produce
    #    the top-k list!!
    return [items[idx] for idx in ordered_indexes[::-1][:k]]


##################################################

class TestPractice(unittest.TestCase):
    """Testing practice problems"""

    def test_normalize_sad(self) -> None:
        """Tests normalize with bad inputs"""

        with self.assertRaises(ValueError):
            normalize([])

        with self.assertRaises(ValueError):
            normalize([1])

        with self.assertRaises(ValueError):
            normalize([1, 1])


    def test_normalize_happy(self) -> None:
        """Tests normalize"""

        self.assertEqual(
            normalize([100, 200]),
            [0, 1]
        )

        #

        inputs: list[float] = [6, 8, 9, 8, 7]
        expected: list[float] = [0, 0.67, 1, 0.67, 0.33]
        actual: list[float] = normalize(inputs)

        for a,e in zip(actual, expected):
            self.assertAlmostEqual(a, e, places=2)

    ###

    def test_topk_sad(self) -> None:
        """Tests top_k with bad inputs"""

        with self.assertRaises(ValueError):
            top_k([], float)

        with self.assertRaises(ValueError):
            top_k(["3.14", "7", "12"], float, k=5)


    def test_topk_happy(self) -> None:
        """Tests top_k with good inputs"""

        self.assertEqual(
            top_k(["3.14", "7", "12"], float),
            ["12", "7", "3.14"]
        )

        self.assertEqual(
            top_k(["3.14", "7", "12", "42"], float),
            ["42", "12", "7"]
        )

        self.assertEqual(
            top_k(["3.14", "7", "12", "42"], float, k=2),
            ["42", "12"]
        )

        self.assertEqual(
            top_k(["3.14", "7", "12", "42"], len, k=1),
            ["3.14"]
        )

        self.assertEqual(
            top_k([8, 6, 7, 5, 3, 0, 9], abs),
            [9, 8, 7]
        )

        self.assertEqual(
            top_k([1, -2, -3, 4], abs),
            [4, -3, -2]
        )

        self.assertEqual(
            top_k(["howdy!!", "ack", "dftba"], lambda x: x, k=2),
            ["howdy!!", "dftba"]
        )

##################################################

if __name__ == "__main__":
    unittest.main()
