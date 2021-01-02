from unittest import TestCase
from p20 import p20

class P20_Test(TestCase):
    def test_10(self):
        self.assertEqual(p20(10), 27)

    def test_100(self):
        self.assertEqual(p20(100), 648)
