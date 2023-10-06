from unittest import TestCase
from p44 import p44

class P44_Test(TestCase):
    def test_result(self):
        self.assertEqual(p44(), 5482660)
