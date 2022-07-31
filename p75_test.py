from unittest import TestCase

from p75 import p75


class P75_Test(TestCase):
    def test_50(self):
        self.assertEqual(p75(51), 6)

    def test_1500000(self):
        self.assertEqual(p75(1500001), 161667)
