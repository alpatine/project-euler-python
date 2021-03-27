from unittest import TestCase
from p29 import p29

class P29_Test(TestCase):
    def test_2_6(self):
        self.assertEqual(p29(6, 6), 15)

    def test_101_101(self):
        self.assertEqual(p29(101, 101), 9183)