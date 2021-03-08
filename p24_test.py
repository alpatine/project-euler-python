from unittest import TestCase
from p24 import p24

class P24_Test(TestCase):
    def test_012_3(self):
        chars = ['0', '1', '2']
        self.assertEqual(p24(chars, 3), ['1', '0', '2'])
    
    def test_1234_13(self):
        chars = ['1', '2', '3', '4']
        expected = ['3', '1', '2', '4']
        self.assertEqual(p24(chars, 13), expected)
    
    def test_0123456789_1000000(self):
        chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        expected = ['2', '7', '8', '3', '9', '1', '5', '4', '6', '0']
        self.assertEqual(p24(chars, 1000000), expected)
