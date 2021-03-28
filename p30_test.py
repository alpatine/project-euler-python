from unittest import TestCase
from p30 import p30

class P30_Test(TestCase):
    def test_4(self):
        self.assertEqual(p30(4), 19316)
    
    def test_5(self):
        self.assertEqual(p30(5), 443839)
