from fractions import Fraction
from unittest import TestCase
from p71 import p71

class P71_Test(TestCase):
    def test_example(self):
        self.assertEqual(p71(8, Fraction(3, 7)), Fraction(2, 5))
    
    def test_result(self):
        self.assertEqual(p71(1000000, Fraction(3, 7)), Fraction(428570,999997))
