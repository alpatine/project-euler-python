from fractions import Fraction
from unittest import TestCase
from p71 import p71

class P71_Test(TestCase):
    def test_example(self):
        self.assertEqual(p71(Fraction(3, 7), 9), Fraction(2, 5))
    
    def test_result(self):
        self.assertEqual(p71(Fraction(3, 7), 1000001), Fraction(428570,999997))
