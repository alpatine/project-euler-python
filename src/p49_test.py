from unittest import TestCase
from p49 import p49

class P49_Test(TestCase):
    def test_result(self):
        expected = [
            [1487, 4817, 8147],
            [2969, 6299, 9629],
        ]
        self.assertEqual(p49(), expected)
