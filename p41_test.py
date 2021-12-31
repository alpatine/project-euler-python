from unittest import TestCase
from p41 import p41

class P41_Test(TestCase):
    def test_result(self):
        self.assertEqual(p41(), 7652413)
