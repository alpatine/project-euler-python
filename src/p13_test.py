from unittest import TestCase
from p13 import P13_NUMBERS, p13

class P13_Test(TestCase):
    def test_1(self):
        self.assertEqual(p13(1, [3]*21), 6)
    
    def test_2(self):
        self.assertEqual(p13(2, [9]*20), 18)

    def test_10(self):
        self.assertEqual(p13(10, P13_NUMBERS), 5537376230)