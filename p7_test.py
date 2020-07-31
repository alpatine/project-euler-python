import unittest
from p7 import p7

class P7_Test(unittest.TestCase):
    def test_p7_6(self):
        self.assertEqual(p7(6), 13)
    
    def test_p7_10001(self):
        self.assertEqual(p7(10001), 104743)
