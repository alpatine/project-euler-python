from unittest import TestCase

from p77 import p77


class P77_Test(TestCase):
    def test_5(self):
        self.assertEqual(p77(5, 11), 10)

    def test_100(self):
        self.assertEqual(p77(5000, 100), 71)
