from unittest import TestCase

from p85 import p85


class P85_Test(TestCase):
    def test_example(self):
        self.assertEqual(p85(18), 6)

    def test_solution(self):
        self.assertEqual(p85(2000000), 2772)
