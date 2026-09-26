from unittest import TestCase

from p90 import p90


class p90_Test(TestCase):
    def test_solution(self):
        self.assertEqual(p90(), 1217)
