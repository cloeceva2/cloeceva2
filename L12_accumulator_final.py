"""
Seeing a (design) pattern!!
"""

from typing import Callable, Generic, Iterable, TypeVar
from collections.abc import Sized

from functools import reduce
from itertools import accumulate

import unittest

############################################################
# 1. Consider the following functions
# 2. Replace them with list comprehensions
#    (that still pass the tests)
############################################################

def excite(phrases: list[str]) -> list[str]:
    """
    Adds ! to the end of all inputs

    Parameters
    ==========
    phrases: list[str]
        phrases to excite

    Returns
    =======
    list[str]
        inputs + "!"
    """

    result = []
    for p in phrases:
        result.append(f'{p}!')

    return result

def super_excite(phrases: list[str]) -> list[str]:
    """
    Adds !!! to the end of all inputs

    Parameters
    ==========
    phrases: list[str]
        phrases to excite

    Returns
    =======
    list[str]
        inputs + "!!!"
    """

    result = []
    for p in phrases:
        result.append(f'{p}!!!')

    return result

def amplify(phrases: list[str]) -> list[str]:
    """
    Converts inputs to CAPS

    Parameters
    ==========
    phrases: list[str]
        phrases to amplify

    Returns
    =======
    list[str]
        INPUTS
    """

    result = []
    for p in phrases:
        result.append(p.upper())

    return result

def how_long(phrases: list[str]) -> list[str]:
    """
    Describes the lengths of the
    inputs

    Parameters
    ==========
    phrases: list[str]
        phrases to describe

    Returns
    =======
    list[str]
        ["k long" (where k is the length of the phrase)]
    """

    result = []
    for p in phrases:
        result.append(f"{len(p)} long")

    return result

############################################################
# 3. Create (and test) one function to rule them ALL!!!!!
#    (termed an "abstraction")
############################################################

T = TypeVar('T')
U = TypeVar('U')

def do_to_all(items: Iterable[T], f: Callable[[T], U]) -> list[U]:
    """
    Applies a function to all the elements of the input
    and returns a list of the resulting outputs

    see: map in Python :)

    Parameters
    ==========
    items: Iterable[T]
        items upon which to do

    f: Callable[[T], U]
        what to do to an item

    Returns
    =======
    list[U]
        list of results
    """

    return [f(i) for i in items]

def make_excitement(how_many: int) -> Callable[[str], str]:
    """
    Creates a function for adding !'s

    Parameters
    ==========
    how_many: int
        how many !'s to add

    Returns
    =======
    Callable[[str], str]:
        function to excite a supplied string

    Raises
    ======
    ValueError
        supplied negative
    """

    if how_many < 0:
        raise ValueError("Must have non-negative excitement")

    def f(phrase: str) -> str:
        return f"{phrase}{ how_many * '!' }"

    return f
    # return lambda phrase: f"{phrase}{ how_many * '!' }"

class Excite(Generic[T]):
    """
    Function object for adding !'s
    """

    def __init__(self, how_excited: int) -> None:
        """
        Initializes Excite object

        Parameters
        ==========
        how_excited: int
            how many !'s to add

        Raises
        ======
        ValueError:
            supplied negative how_excited
        """

        if how_excited < 0:
            raise ValueError("Must have non-negative excitement")

        self._n: int = how_excited

    def __call__(self, phrase: str) -> str:
        """
        Adds !'s to the end of the supplied
        phrase, based upon object init

        Parameters
        ==========
        phrase: str
            input phrase

        Returns
        =======
        str: 
            resulting excitement
        """

        return f"{phrase}{ '!' * self._n }"

    def __str__(self) -> str:
        """Human-readable string"""

        return f"Excite({self._n})"


############################################################
# 4. Consider the following functions
# 5. Replace them with list comprehensions
#    (that still pass the tests)
############################################################

def keep_positive(nums: list[int]) -> list[int]:
    """
    Keeps only positive numbers

    Parameters
    ==========
    nums: list[int]
        input numbers

    Returns
    =======
    list[int]
        subset that are positive
    """

    result = []
    for n in nums:
        if n > 0:
            result.append(n)

    return result

def keep_palindromic(nums: list[int]) -> list[int]:
    """
    Keeps only numbers that are the same forward/backward

    Parameters
    ==========
    nums: list[int]
        input numbers

    Returns
    =======
    list[int]
        subset that are palindromic
    """

    result = []
    for n in nums:
        if str(n) == str(n)[::-1]:
            result.append(n)

    return result

############################################################
# 6. Abstract!!
############################################################

def keep_if(items: Iterable[T], p: Callable[[T], bool]) -> list[T]:
    """
    Produces the subset of the items
    that satisfy the predicate

    see: filter in Python :)

    Parameters
    ==========
    items: Iterable[T]
        items to consider

    p: Callable[[T], bool]
        predicate to apply

    Return
    ======
    list[T]:
        those items for which
        p returns True
    """

    return [i for i in items if p(i)]


############################################################
# 7. Consider the following functions - abstract!!
# 8. For an extra challenge, can you come up with a
#    way to use your new abstraction to implement
#    your last two?
############################################################

def my_sum(nums: list[int]) -> int:
    """
    Adds all the numbers
    in the list

    Parameters
    ==========
    nums: list[int]
        numbers to sum

    Returns
    =======
    int
        sum of the numbers
    """

    result: int = 0

    for n in nums:
        result += n

    return result

def my_len(items: list[T]) -> int:
    """
    Counts the items in the list

    Parameters
    ==========
    items: list[T]

    Returns
    =======
    int
        how many?
    """

    result: int = 0

    for _ in items:
        result += 1

    return result

def any_dftba(phrases: list[str]) -> bool:
    """
    Determines if any of
    the phrases are
    "dftba" (case-insensitive)

    see: any/all in Python :)

    Parameters
    ==========
    phrases: list[str]
        input phrases

    Returns
    =======
    bool:
        is "dftba" found in any case?
    """

    result: bool = False

    for p in phrases:
        if p.lower() == "dftba":
            result = True

    return result

def combine(items: Iterable[T], f: Callable[[U, T], U], init: U) -> U:
    """
    Abstraction over accumulator
    pattern

    see: functools.reduce, itertools.accumulate :)

    Parameters
    ==========
    items: Iterable[T]
        items to process

    f: Callable[[U, T], U]
        function that can process
        a single item with a prior
        result

    init: U
        result to start with

    Returns
    =======
    U
        result of accumulation
    """

    result: U = init

    for i in items:
        result = f(result, i)

    return result

############################################################
############################################################

class TestPattern(unittest.TestCase):
    """Tests ALL the patterns"""

    def test_excite(self) -> None:
        """Tests excite function"""

        self.assertEqual(excite([]), [])
        self.assertEqual(excite(['', 'a', 'bb', 'ccc']), ['!', 'a!', 'bb!', 'ccc!'])

    def test_super_excite(self) -> None:
        """Tests super_excite function"""

        self.assertEqual(super_excite([]), [])
        self.assertEqual(super_excite(['', 'a', 'bb', 'ccc']), ['!!!', 'a!!!', 'bb!!!', 'ccc!!!'])

    def test_amplify(self) -> None:
        """Tests amplify function"""

        self.assertEqual(amplify([]), [])
        self.assertEqual(amplify(['', 'a', 'bb', 'ccc']), ['', 'A', 'BB', 'CCC'])

    def test_how_long(self) -> None:
        """Tests how_long function"""

        self.assertEqual(how_long([]), [])
        self.assertEqual(how_long(['', 'a', 'bb', 'ccc']), ['0 long', '1 long', '2 long', '3 long'])

    ###

    def test_do_to_all(self) -> None:
        """Tests do_to_all"""

        self.assertEqual(
            do_to_all([], len),
            list(map(len, []))
        )

        self.assertEqual(
            do_to_all([], len),
            []
        )

        #

        input_phrases = ('', 'a', 'bb', 'ccc')

        self.assertEqual(
            do_to_all(input_phrases, len),
            list(map(len, input_phrases))
        )

        f_excite1: Callable[[str], str] = Excite(1)
        f_excite3: Callable[[str], str] = make_excitement(3)

        self.assertEqual(
            do_to_all(input_phrases, f_excite1),
            list(map(f_excite1, input_phrases))
        )

        self.assertEqual(
            do_to_all(input_phrases, f_excite3),
            list(map(f_excite3, input_phrases))
        )

        describe_phrase: Callable[[str], str] = lambda p: f"{len(p)} long"

        self.assertEqual(
            do_to_all(input_phrases, describe_phrase),
            list(map(describe_phrase, input_phrases))
        )

        self.assertEqual(
            do_to_all(input_phrases, str.upper),
            list(map(str.upper, input_phrases))
        )

    ###

    def test_keep_positive(self) -> None:
        """Tests keep_positive"""

        self.assertEqual(keep_positive([]), [])
        self.assertEqual(keep_positive([0, -1, 2, -3, -4, 5]), [2, 5])

    def test_keep_palindromic(self) -> None:
        """Tests keep_palindromic"""

        self.assertEqual(keep_palindromic([]), [])
        self.assertEqual(keep_palindromic([0, -1, 2, 100, 101]), [0, 2, 101])

    def test_keep_if(self) -> None:
        """Tests keep_if"""

        non_empty: Callable[[Sized], bool] = lambda i: len(i) > 0
        is_pos: Callable[[float], bool] = lambda n: n > 0
        is_palindromic: Callable[[T], bool] = lambda x: str(x) == str(x)[::-1]

        s_list = ('', 'a', 'bb', 'ccc')
        n_list1 = (0, -1, 2, -3, -4, 5)
        n_list2 = (0, -1, 2, 100, 101)

        self.assertEqual(keep_if([], lambda _: True), [])
        self.assertEqual(
            keep_if([], lambda _: True),
            list(filter(non_empty, []))
        )

        self.assertEqual(
            keep_if(s_list, non_empty),
            list(filter(non_empty, s_list))
        )

        self.assertEqual(
            keep_if(s_list, is_palindromic),
            list(filter(is_palindromic, s_list))
        )

        self.assertEqual(
            keep_if(n_list1, is_pos),
            list(filter(is_pos, n_list1))
        )

        self.assertEqual(
            keep_if(n_list2, is_pos),
            list(filter(is_pos, n_list2))
        )

        self.assertEqual(
            keep_if(n_list1, is_palindromic),
            list(filter(is_palindromic, n_list1))
        )

        self.assertEqual(
            keep_if(n_list2, is_palindromic),
            list(filter(is_palindromic, n_list2))
        )

    #

    def test_my_sum(self) -> None:
        """Tests my_sum"""

        self.assertEqual(my_sum([]), 0)
        self.assertEqual(my_sum([1, 2, 3, 4, 5, -6]), 9)

    def test_my_len(self) -> None:
        """Tests my_len"""

        self.assertEqual(my_len([]), 0)
        self.assertEqual(my_len([1, 2, 3, 4, 5, -6]), 6)

    def test_any_dftba(self) -> None:
        """Tests any_dftba"""

        self.assertEqual(any_dftba([]), False)
        self.assertEqual(any_dftba(['', 'a', 'bb', 'ccc']), False)
        self.assertEqual(any_dftba(['DFTBA']), True)
        self.assertEqual(any_dftba(['nope', 'DFtbA', 'NO']), True)

    #

    def test_combine(self) -> None:
        """Tests combine"""

        add_str: Callable[[str, str], str] = lambda acc_old, val_new: acc_old + val_new
        add_int: Callable[[int, int], int] = lambda acc_old, val_new: acc_old + val_new
        add_1: Callable[[int, int], int] = lambda acc_old, _: acc_old + 1
        or_dftba: Callable[[bool, str], bool] = \
            lambda acc_old, val_new: acc_old or (val_new.lower() == "dftba")

        self.assertEqual(combine([], str.__add__, ""), "")
        self.assertEqual(
            combine(
                ['', 'a', 'bb', 'ccc'],
                add_str,
                ""
            ),
            reduce(
                add_str,
                ['', 'a', 'bb', 'ccc'],
                ""
            )
            # "abbccc"
        )
        self.assertEqual(
            combine(
                ['', 'a', 'bb', 'ccc'],
                add_str,
                ""
            ),
            list(accumulate(
                ['', 'a', 'bb', 'ccc'],
                add_str,
                initial=""
            ))[-1]
            # "abbccc"
        )

        self.assertEqual(
            combine([], add_int, 0),
            reduce(add_int, [], 0)
            # 0
        )

        self.assertEqual(
            combine(
                [1, 2, 3, 4, 5, -6],
                add_int,
                0
            ),
            reduce(
                add_int,
                [1, 2, 3, 4, 5, -6],
                0
            )
            # 9
        )

        self.assertEqual(
            combine(
                [1, 2, 3, 4, 5, -6],
                add_1,
                0
            ),
            reduce(
                add_1,
                [1, 2, 3, 4, 5, -6],
                0
            )
            # 6
        )

        self.assertEqual(
            combine(
                ['', 'a', 'bb', 'ccc'],
                or_dftba,
                False
            ),
            reduce(
                or_dftba,
                ['', 'a', 'bb', 'ccc'],
                False
            )
            # False
        )

        self.assertEqual(
            combine(
                ['DFTBA'],
                or_dftba,
                False
            ),
            reduce(
                or_dftba,
                ['DFTBA'],
                False
            )
            # True
        )

        self.assertEqual(
            combine(
                ['nope', 'DFtbA', 'NO'],
                or_dftba,
                True
            ),
            reduce(
                or_dftba,
                ['nope', 'DFtbA', 'NO'],
                True
            )
            # True
        )

if __name__ == "__main__":
    unittest.main()
