from fractions import Fraction
from unittest import TestCase

from continued_fractions import convergents


class Convergents_Test(TestCase):
    def test_2_4(self):
        # 9/4 = [2; 4]
        expected = [
            Fraction(2, 1),
            Fraction(9, 4),
        ]
        self.assertEqual(list(convergents([2, 4])), expected)

    def test_0_2_4(self):
        # 4/9 = [0; 2, 4]
        expected = [
            Fraction(0, 1),
            Fraction(1, 2),
            Fraction(4, 9),
        ]
        self.assertEqual(list(convergents([0, 2, 4])), expected)
    
    def test_0_1_5_2_2(self):
        # 0.84375 = 27/32 = [0; 1, 5, 2, 2]
        expected = [
            Fraction(0, 1),
            Fraction(1, 1),
            Fraction(5, 6),
            Fraction(11, 13),
            Fraction(27, 32),
        ]
        self.assertEqual(list(convergents([0, 1, 5, 2, 2])), expected)
    
    def test_1_1_2_1_2_1_2_1_2(self):
        # sqrt(3) = [1; 1, 2, 1, 2, 1, 2, 1, 2, ...]
        expected = [
            Fraction(1, 1),
            Fraction(2, 1),
            Fraction(5, 3),
            Fraction(7, 4),
            Fraction(19, 11),
            Fraction(26, 15),
            Fraction(71, 41),
            Fraction(97, 56),
        ]
        self.assertEqual(list(convergents([1, 1, 2, 1, 2, 1, 2, 1])),
                         expected)
    
    def test_3_4_12_4(self):
        # 3.245 = 649/200 = [3; 4, 12, 4]
        expected = [
            Fraction(3, 1),
            Fraction(13, 4),
            Fraction(159,49),
            Fraction(649, 200),
        ]
        self.assertEqual(list(convergents([3, 4, 12, 4])), expected)
