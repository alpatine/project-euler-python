from unittest import TestCase
from p42 import p42

class P42_Test(TestCase):
    def test_result(self):
        self.assertEqual(p42(), 162)
