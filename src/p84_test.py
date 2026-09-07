from unittest import TestCase

from p84 import p84


class P84_Test(TestCase):
    def test_example(self):
        self.assertEqual(p84(6), '102400')

    def test_solution(self):
        self.assertEqual(p84(4), '101524')
