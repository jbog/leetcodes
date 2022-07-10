import pytest
from solution import Solution
solution = Solution()

def test_example1():
    assert solution.romanToInt("III") == 3

def test_example2():
    assert solution.romanToInt("LVIII") == 58

def test_example3():
    assert solution.romanToInt("MCMXCIV") == 1994
