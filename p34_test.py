from unittest import TestCase
from p34 import p34

class P34_Test(TestCase):
    def test_p34(self):
        self.assertEqual(p34(), 40730)
        