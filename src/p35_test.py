from unittest import TestCase
from p35 import p35

class P35_Test(TestCase):
    def test_100(self):
        self.assertEqual(p35(100), 13)

    def test_1000000(self):
        self.assertEqual(p35(1000000), 55)
