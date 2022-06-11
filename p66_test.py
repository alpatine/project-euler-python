from unittest import TestCase
from p66 import p66

class P66_Test(TestCase):
    def test_7(self):
        self.assertEqual(p66(7), 5)
    
    def test_1000(self):
        self.assertEqual(p66(1001), 661)
