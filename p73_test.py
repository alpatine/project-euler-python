from fractions import Fraction
from unittest import TestCase
from p73 import p73

class P73_Test(TestCase):
    def test_example(self):
        left = Fraction(1, 3)
        right = Fraction(1, 2)
        expected = 3
        max_denominator = 8
        self.assertEqual(p73(max_denominator, left, right), expected)

    def test_result(self):
        left = Fraction(1, 3)
        right = Fraction(1, 2)
        expected = 7295372
        max_denominator = 12000
        self.assertEqual(p73(max_denominator, left, right), expected)