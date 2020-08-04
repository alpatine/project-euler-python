from unittest import TestCase
from p2 import p2

class P2_Test(TestCase):
    def test_p2_90(self):
        self.assertEqual(p2(90), 44)
    
    def test_p2_4000001(self):
        self.assertEqual(p2(4000001), 4613732)
