from unittest import TestCase

from p80 import p80


class P80_Test(TestCase):
    def test_example(self):
        self.assertEqual(p80(2, 3), 475)

    def test_solution(self):
        self.assertEqual(p80(1, 101), 40886)
