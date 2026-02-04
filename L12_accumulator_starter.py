"""
Seeing a (design) pattern!!
"""

import unittest
from typing import Callable

############################################################
# 1. Consider the following functions
# 2. Replace them with list comprehensions
#    (that still pass the tests)
############################################################

#thing 1: ??? = f'{p}!'
# thing 2: ??? = f'{p}!!!'
# thing3 : ??? = p.upper()
# thing4: ??? = f'{len(p)} long'

def f_excite(p):
    return f'{p}!'
def f_superexcite(p):
    return f'{p}!!!'
def f_aplify(p):
    return p.upper()
def f_howlong(p):
    return f'{len(p)} long'


thing1: Callable[[str],str] = f'{p}!'
thing2: Callable[[str],str] = f'{p}!!!'
thing3 : Callable[[str],str] = p.upper()
thing4: Callable[[str],str] = f'{len(p)} long'


def abstract_whatever(phrases: list[str], thing: Callable[[str],str])-> list[str]:
    return [thing(p) for p in phrases]

#return [thing1 for p in phrases]
#return [thing2 for p in phrases]
#return [thing3 for p in phrases]
#return [thing4 for p in phrases]





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

    #return [do_exp for ?? in ??? if_exp]
    return [f'{p}!' for p in phrases]

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
    return [f'{p}!!!' for p in phrases]
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
    return [p.upper() for p in phrases]
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
    return ["{len(p)} long" for p in phrases]
    result = []
    for p in phrases:
        result.append(f"{len(p)} long")

    return result

############################################################
# 3. Create (and test) one function to rule them ALL!!!!!
#    (termed an "abstraction")
############################################################

# TODO: do_to_all
def do_to_all(phrases: list[str], f: Callable[[str],str])-> list[str]:
    """
      Does somthing to each element in supplied list
     
     Parameters
     ==========
     phrases: list[str]
        input[list]
     p: Callable[[T], bool]
        predicate to apply

    Return
    ======
    list[T]:
        those items for which
        p returns True

    """
    return [f(p) for p in phrases]

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

# TODO: keep_if

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

def my_len(items: list[int]) -> int:
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

# TODO: combine

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

    # TODO: test do_to_all
    def test_do_to_all(self)-> None:
        inputs = [ '', 'a', 'bb', 'ccc']
            self.assertEqual(
                excite(inputs)

            )
]

    ###

    def test_keep_positive(self) -> None:
        """Tests keep_positive"""

        self.assertEqual(keep_positive([]), [])
        self.assertEqual(keep_positive([0, -1, 2, -3, -4, 5]), [2, 5])

    def test_keep_palindromic(self) -> None:
        """Tests keep_palindromic"""

        self.assertEqual(keep_palindromic([]), [])
        self.assertEqual(keep_palindromic([0, -1, 2, 100, 101]), [0, 2, 101])

    # TODO: test keep_if

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

    # TODO: test combine

if __name__ == "__main__":
    unittest.main()
