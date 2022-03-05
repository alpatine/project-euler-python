from unittest import TestCase
from p48 import p48

class P48_Test(TestCase):
    def test(self):
        self.assertEqual(p48(11), 405071317)

    def test_1000(self):
        self.assertEqual(p48(1001), 9110846700)