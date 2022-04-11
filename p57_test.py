from unittest import TestCase
from p57 import p57

class P57_Test(TestCase):
    def test_4(self):
        self.assertEqual(p57([1] + [2] * 4), 0)
    
    def test_8(self):
        self.assertEqual(p57([1] + [2] * 8), 1)
    
    def test_1000(self):
        self.assertEqual(p57([1] + [2] * 1000), 153)
