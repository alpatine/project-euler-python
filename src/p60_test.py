from unittest import TestCase
from p60 import p60

class P60_Test(TestCase):
    def test_4(self):
        self.assertEqual(p60(4, 1000, 1000000), 792)
    
    def test_5(self):
        self.assertEqual(p60(5, 10000, 1000000), 26033)
