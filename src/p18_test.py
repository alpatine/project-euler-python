from unittest import TestCase
from p18 import p18, P18_TRIANGLE

class P18_Test(TestCase):
    def test_given(self):
        triangle_to_test = [[3],
                            [7, 4],
                            [2, 4, 6],
                            [8, 5, 9, 3]]
        self.assertEqual(p18(triangle_to_test), 23)
    
    def test_problem(self):
        triangle_to_test = P18_TRIANGLE
        self.assertEqual(p18(triangle_to_test), 1074)
