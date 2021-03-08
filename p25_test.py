from unittest import TestCase
from p25 import p25

class P25_Test(TestCase):
    def test_2(self):
        self.assertEqual(p25(2), 7)
    
    def test_3(self):
        self.assertEqual(p25(3), 12)
    
    def test_1000(self):
        self.assertEqual(p25(1000), 4782)