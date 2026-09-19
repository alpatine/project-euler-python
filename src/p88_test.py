from unittest import TestCase

from p88 import p88


class p88_Test(TestCase):
    def test_example_6(self):
        self.assertEqual(p88(6), 30)

    def test_example_12(self):
        self.assertEqual(p88(12), 61)

    def test_solution(self):
        self.assertEqual(p88(12000), 7587457)
