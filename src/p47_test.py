from unittest import TestCase
from p47 import p47

class P47_Test(TestCase):
    def test_2(self):
        self.assertEqual(p47(2, 21), 14)
    
    def test_3(self):
        self.assertEqual(p47(3, 701), 644)

    def test_4(self):
        self.assertEqual(p47(4, 134051), 134043)
