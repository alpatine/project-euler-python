from unittest import TestCase
from p62 import p62

class P62_Test(TestCase):
    def test_3_permutations(self):
        self.assertEqual(p62(3), 41063625)
    
    def test_5_permutations(self):
        self.assertEqual(p62(5), 127035954683)
