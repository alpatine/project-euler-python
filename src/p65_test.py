from unittest import TestCase
from p65 import p65

class P65_Test(TestCase):
    def test_result(self):
        self.assertEqual(p65(), 272)
