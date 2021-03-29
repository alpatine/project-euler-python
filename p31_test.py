from unittest import TestCase
from p31 import p31

class P31_Test(TestCase):
    def test_1_1(self):
        self.assertEqual(p31(1, [1]), 1)

    def test_6_5_2_1(self):
        self.assertEqual(p31(6, [5, 2, 1]), 5)

    def test_200_1_2_5_10_20_50_100_200(self):
        self.assertEqual(p31(200, [1, 2, 5, 10, 20, 50, 100, 200]), 73682)
