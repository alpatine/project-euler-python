from unittest import TestCase
from p40 import p40

class P40_Test(TestCase):
    def test_1(self):
        self.assertEqual(p40([1]), 1)
    
    def test_1_5(self):
        self.assertEqual(p40([1, 5]), 5)
    
    def test_0_3(self):
        self.assertEqual(p40([0, 3]), 0)

    def test_answer(self):
        self.assertEqual(p40([1, 10, 100, 1000, 10000, 100000, 1000000]), 210)
