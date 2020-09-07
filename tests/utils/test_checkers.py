import pytest
from src.utils.checkers import integer_checker, float_checker, string_checker

class TestTypeChecker(object):
    def test_integer_checker(self):
        actual = isinstance(integer_checker(10), int)
        assert actual == True, f'Expected: True, Actual: {actual}'

    def test_float_checker(self):
        actual = isinstance(float_checker(10.0), float)
        assert actual == True, f'Expected: True, Actual: {actual}'

    def test_string_checker(self):
        actual = isinstance(string_checker('Daniel'), str)
        assert actual == True, f'Expected: True, Actual: {actual}'
