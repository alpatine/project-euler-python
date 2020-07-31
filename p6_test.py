import unittest
from p6 import p6

class P6_Test(unittest.TestCase):
    def test_p6_11(self):
        self.assertEqual(p6(11), 2640)
        
    def test_p6_101(self):
        self.assertEqual(p6(101), 25164150)
