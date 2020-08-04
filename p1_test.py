from unittest import TestCase
from p1 import p1

class P1_Test(TestCase):
    def test_p1_10(self):
        self.assertEqual(p1(10), 23)
    
    def test_p1_1000(self):
        self.assertEqual(p1(1000), 233168)
