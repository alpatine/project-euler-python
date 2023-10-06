from unittest import TestCase
from p67 import load_triangle, p67

class P67_Test(TestCase):
    GIVEN_PATH = './data/p067_triangle_given.txt'
    def test_load_triangle(self):
        path = P67_Test.GIVEN_PATH
        expected = [[3],
                    [7, 4],
                    [2, 4, 6],
                    [8, 5, 9, 3]]
        self.assertEqual(load_triangle(path), expected)
    
    def test_given(self):
        path = P67_Test.GIVEN_PATH
        self.assertEqual(p67(path), 23)

    def test_result(self):
        path = './data/p067_triangle.txt'
        self.assertEqual(p67(path), 7273)
