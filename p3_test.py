import unittest
from p3 import p3

class P3_Test(unittest.TestCase):
    def test_p3_13195(self):
        self.assertEqual(p3(13195), 29)
    
    def test_p3_600851475143(self):
        self.assertEqual(p3(600851475143), 6857)