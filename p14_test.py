from unittest import TestCase
from p14 import p14

class P14_Test(TestCase):
    def test_1_1000000(self):
        self.assertEqual(p14(1000000), 837799)
