from unittest import TestCase
from p39 import p39

class P39_Test(TestCase):
    def test_12(self):
        self.assertEqual(p39(13), 12)
    
    def test_120(self):
        self.assertEqual(p39(121), 120)
    
    def test_1000(self):
        self.assertEqual(p39(1001), 840)