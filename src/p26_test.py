from unittest import TestCase
from p26 import p26

class P26_Test(TestCase):
    def test_10(self):
        self.assertEqual(p26(10), 7)
    
    def test_1000(self):
        self.assertEqual(p26(1000), 983)
