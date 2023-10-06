from unittest import TestCase
from p58 import p58

class P58_Test(TestCase):
    def test_0_5(self):
        self.assertEqual(p58(0.5), 11)

    def test_0_1(self):
        self.assertEqual(p58(0.1), 26241)
