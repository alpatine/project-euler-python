from unittest import TestCase
from p56 import p56

class P56_Test(TestCase):
    def test_result(self):
        self.assertEqual(p56(), 972)
