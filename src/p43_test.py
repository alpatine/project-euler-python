from unittest import TestCase
from p43 import p43

class P43_Test(TestCase):
    def test_result(self):
        self.assertEqual(p43(), 16695334890)
