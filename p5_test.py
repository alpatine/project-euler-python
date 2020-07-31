import unittest
from p5 import p5

class P5_Test(unittest.TestCase):
    def test_p5_11(self):
        self.assertEqual(p5(11), 2520)
    
    def test_p5_21(self):
        self.assertEqual(p5(21), 232792560)