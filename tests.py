import unittest
from p1 import p1

class P1Test(unittest.TestCase):
    def test_10(self):
        self.assertEqual(p1(10), 23)
    
    def test_1000(self):
        self.assertEqual(p1(1000), 233168)
