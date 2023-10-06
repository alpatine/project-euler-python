from unittest import TestCase
from p19 import p19

class P19_Test(TestCase):
    
    def test_problem(self):
        self.assertEqual(p19(), 171)
