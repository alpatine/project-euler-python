from unittest import TestCase

from p74 import p74


class P74_Test(TestCase):
    def test_10_1(self):
        self.assertEqual(p74(10, 1), 2)

    def test_10_16(self):
        self.assertEqual(p74(10, 16), 1)

    def test_1000000_60(self):
        self.assertEqual(p74(1000000, 60), 402)
