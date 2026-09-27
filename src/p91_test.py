from unittest import TestCase

from p91 import p91


class p91_Test(TestCase):
    def test_example_2(self):
        self.assertEqual(p91(2), 14)

    def test_3(self):
        self.assertEqual(p91(3), 33)

    def test_solution(self):
        self.assertEqual(p91(50), 14234)
