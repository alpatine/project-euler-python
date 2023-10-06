from unittest import TestCase
from p45 import p45

class P45_Test(TestCase):
    def test_first(self):
        self.assertEqual(p45(1, 10), 1)
    
    def test_second(self):
        self.assertEqual(p45(10, 1000), 40755)
    
    def test_third(self):
        self.assertEqual(p45(1000, 100000), 1533776805)
