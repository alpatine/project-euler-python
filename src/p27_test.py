from unittest import TestCase
from p27 import p27

class P27_Test(TestCase):
    def test_1_2_41_42(self):
        self.assertEqual(p27(1, 2, 41, 42), 41)
    
    def test_n79_n78_1601_1602(self):
        self.assertEqual(p27(-79, -78, 1601, 1602), -126479)

    def test_n999_1000_n1000_1001(self):
        self.assertEqual(p27(-999, 1000, -1000, 1001), -59231)
