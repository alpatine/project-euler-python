from unittest import TestCase
from p15 import p15

class P15_Test(TestCase):
    def test_1(self):
        self.assertEqual(p15(1), 2)
    
    def test_2(self):
        self.assertEqual(p15(2), 6)
    
    def test_3(self):
        self.assertEqual(p15(3), 20)

    def test_20(self):
        self.assertEqual(p15(20), 137846528820)
