from unittest import TestCase
from p72 import p72

class P72_Test(TestCase):
    def test_3(self):
        self.assertEqual(p72(3), 3)
    
    def test_5(self):
        self.assertEqual(p72(5), 9)
    
    def test_8(self):
        self.assertEqual(p72(8), 21)

    def test_1000000(self):
        self.assertEqual(p72(1000000), 303963552391)
