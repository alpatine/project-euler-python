from unittest import TestCase

from p87 import p87


class p87_Test(TestCase):
    def test_example(self):
        self.assertEqual(p87(50), 4)

    def test_solution(self):
        self.assertEqual(p87(50000000), 1097343)
