from unittest import TestCase
from p50 import p50

class P50_Test(TestCase):
    def test_101(self):
        self.assertEqual(p50(101), 41)
    
    def test_1001(self):
        self.assertEqual(p50(1001), 953)
    
    def test_1000001(self):
        self.assertEqual(p50(1000001), 997651)
