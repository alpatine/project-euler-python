from unittest import TestCase
from p53 import p53

class P53_Test(TestCase):
    def test_1_5_4(self):
        self.assertEqual(p53(1, 6, 4), 5)
    
    def test_6_6_10(self):
        self.assertEqual(p53(6, 7, 10), 3)
    
    def test_6_7_10(self):
        self.assertEqual(p53(6, 8, 10), 7)
    
    def test_1_100_1000000(self):
        self.assertEqual(p53(1, 101, 1000000), 4075)