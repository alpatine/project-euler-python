from unittest import TestCase

from p78 import p78


class P78_Test(TestCase):
    def test_7_11(self):
        self.assertEqual(p78(7, 11), 5)

    def test_1000000_100000(self):
        self.assertEqual(p78(1000000, 100000), 55374)
