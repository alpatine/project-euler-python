from unittest import TestCase
from p36 import p36

class P36_Test(TestCase):
    def test_10(self):
        self.assertEqual(p36(10), 25)
    
    def test_40(self):
        self.assertEqual(p36(40), 58)
    
    def test_1000000(self):
        self.assertEqual(p36(1000000), 872187)
