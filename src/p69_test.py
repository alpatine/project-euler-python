from unittest import TestCase
from p69 import p69

class P69_Test(TestCase):
    def test_example(self):
        self.assertEqual(p69(11), 6)
    
    def test_result(self):
        self.assertEqual(p69(1000001), 510510)
