from unittest import TestCase

from p76 import p76


class P76_Test(TestCase):
    def test_5(self):
        self.assertEqual(p76(5), 6)

    def test_100(self):
        self.assertEqual(p76(100), 190569291)
