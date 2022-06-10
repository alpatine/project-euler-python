from unittest import TestCase
from p64 import p64

class P64_Test(TestCase):
    def test_13(self):
        self.assertEqual(p64(14), 4)

    def test_10000(self):
        self.assertEqual(p64(10001), 1322)
