from unittest import TestCase
from p70 import p70

class P70_Test(TestCase):
    def test_result(self):
        self.assertEqual(p70(10**7), 8319823)
