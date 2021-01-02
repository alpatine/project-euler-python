from unittest import TestCase
from p17 import p17

class P17_Test(TestCase):
    def test_5(self):
        self.assertEqual(p17(6), 19)
    
    def test_1000(self):
        self.assertEqual(p17(1001), 21124)
