from unittest import TestCase
from p28 import p28

class P28_Test(TestCase):
    def test_1(self):
        self.assertEqual(p28(1), 1)

    def test_2(self):
        self.assertEqual(p28(2), 25)
    
    def test_3(self):
        self.assertEqual(p28(3), 101)

    def test_501(self):
        self.assertEqual(p28(501), 669171001)
