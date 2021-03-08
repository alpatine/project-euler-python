from unittest import TestCase
from p23 import p23

class P23_Test(TestCase):
    def test_2(self):
        self.assertEqual(p23(2), 1)

    def test_25(self):
        self.assertEqual(p23(25), 276)
    
    def test_28124(self):
        self.assertEqual(p23(28124), 4179871)