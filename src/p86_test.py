from unittest import TestCase

from p86 import p86


class p86_Test(TestCase):
    def test_example(self):
        self.assertEqual(p86(2000), 100)

    def test_solution(self):
        self.assertEqual(p86(1000000), 1818)
