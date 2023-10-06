from unittest import TestCase
from p16 import p16

class P16_Test(TestCase):
    def test_2_15(self):
        self.assertEqual(p16(2, 15), 26)
    
    def test_2_1000(self):
        self.assertEqual(p16(2, 1000), 1366)