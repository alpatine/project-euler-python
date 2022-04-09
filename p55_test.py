from unittest import TestCase
from p55 import p55

class P55_Test(TestCase):
    def test_result(self):
        self.assertEqual(p55(10000), 249)
