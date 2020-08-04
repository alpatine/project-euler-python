from unittest import TestCase
from p9 import p9

class P9_Test(TestCase):
    def test_p9_12(self):
        self.assertEqual(p9(12), 60)

    def test_p9_24(self):
        self.assertEqual(p9(24), 480)
    
    def test_p9_1000(sefl):
        sefl.assertEqual(p9(1000), 31875000)