from unittest import TestCase
from p63 import p63

class P63_Test(TestCase):
    def test_result(self):
        self.assertEqual(p63(), 49)