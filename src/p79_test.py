from unittest import TestCase

from p79 import p79


class P79_Test(TestCase):
    def test_problem(self):
        self.assertEqual(p79('./data/p0079_keylog.txt'), '73162890')
