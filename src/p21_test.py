from unittest import TestCase
from p21 import p21

class P21_Test(TestCase):
    def test_301(self):
        self.assertEqual(p21(301), 504)
    
    def test_10000(self):
        self.assertEqual(p21(10000), 31626)
