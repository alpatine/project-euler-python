import unittest
from p4 import p4

class P4_Test(unittest.TestCase):
    def test_p4_2(self):
        self.assertEqual(p4(2), 9009)

    def test_p4_3(self):
        self.assertEqual(p4(3), 906609)
