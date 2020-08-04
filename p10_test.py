from unittest import TestCase
from p10 import p10

class P10_Test(TestCase):
    def test_p10_10(self):
        self.assertEqual(p10(10), 17)
    
    def test_p10_2000000(self):
        self.assertEqual(p10(2000000), 142913828922)