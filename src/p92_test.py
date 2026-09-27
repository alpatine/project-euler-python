from unittest import TestCase

from p92 import p92


class p92_Test(TestCase):
    def test_solution(self):
        self.assertEqual(p92(10000000), 8581146)
