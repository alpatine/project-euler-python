from unittest import TestCase
from p12 import p12

class P12_Test(TestCase):
    def test_1(self):
        self.assertEqual(p12(1), 1)
    
    def test_2(self):
        self.assertEqual(p12(2), 3)
    
    def test_4(self):
        self.assertEqual(p12(4), 6)
    
    def test_6(self):
        self.assertEqual(p12(6), 28)
    
    def test_500(self):
        self.assertEqual(p12(500), 76576500)
