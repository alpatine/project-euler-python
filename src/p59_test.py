from unittest import TestCase
from p59 import p59

class P59_Test(TestCase):
    def test_result(self):
        self.assertEqual(p59(), 129448)
