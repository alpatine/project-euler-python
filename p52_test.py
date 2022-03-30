from unittest import TestCase
from p52 import p52

class P52_Test(TestCase):
    def test_result(self):
        self.assertEqual(p52(6), 142857)
