from unittest import TestCase
from p11 import p11, P11_GRID

class P11_Test(TestCase):
    def test_p11_horizontal_3(self):
        grid = [ [  0,  1,  2,  3],
                 [  4,  5,  6,  7],
                 [ 99, 99, 99,  0],
                 [ 12, 13, 14, 15] ]
        
        self.assertEqual(p11(grid, 3), 970299)

    def test_p11_vertical_3(self):
        grid = [ [  0,  1,  2,  3],
                 [ 99,  4,  5,  6],
                 [ 99,  7,  8,  9],
                 [ 99, 10, 11, 12] ]
        
        self.assertEqual(p11(grid, 3), 970299)
    
    def test_p11_SE_diagonal_3(self):
        grid = [ [  0, 99,  1,  2],
                 [  3,  4, 99,  5],
                 [  6,  7,  8, 99],
                 [  9, 10, 11, 12] ]
        
        self.assertEqual(p11(grid, 3), 970299)
    
    def test_p11_SW_diagonal_3(self):
        grid = [ [  0,  1,  2,  3],
                 [  4,  5, 99,  6],
                 [  7, 99,  8,  9],
                 [ 99, 10, 11, 12] ]
        
        self.assertEqual(p11(grid, 3), 970299)
    
    def test_p11_4(self):
        self.assertEqual(p11(P11_GRID, 4), 70600674)