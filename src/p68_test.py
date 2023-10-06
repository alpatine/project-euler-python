from unittest import TestCase

from p68 import calculate_ngon_str, generate_ngons, p68


class P68_Test(TestCase):
    # ngon format - first half of the array are the outer values in
    # clockwise order starting with the smallest, then the second half
    # are the inner values attached to the outer values in the same order

    def test_generate_3_gons(self):
        correct_3_gons = [
            [1, 2, 3, 5, 6, 4],
            [1, 3, 2, 6, 5, 4],
            [1, 3, 5, 4, 6, 2],
            [1, 5, 3, 6, 4, 2],
            [2, 4, 6, 3, 5, 1],
            [2, 6, 4, 5, 3, 1],
            [4, 5, 6, 2, 3, 1],
            [4, 6, 5, 3, 2, 1],
        ]
        ngons = generate_ngons(3)
        for correct_ngon in correct_3_gons:
            self.assertIn(correct_ngon, ngons)
    
    def test_generate_5_gons(self):
        correct_5_gons = [
            [1, 2, 3, 4, 5, 8, 10, 7, 9, 6],
            [1, 3, 5, 7, 9, 6, 10, 4, 8, 2],
            [1, 5, 4, 3, 2, 10, 8, 6, 9, 7],
            [1, 9, 7, 5, 3, 10, 6, 2, 8, 4],
            [2, 4, 6, 8, 10, 5, 9, 3, 7, 1],
            [2, 5, 3, 6, 9, 7, 8, 4, 10, 1],
            [2, 5, 8, 6, 9, 4, 10, 1, 7, 3],
            [2, 9, 6, 3, 5, 8, 7, 1, 10, 4],
            [2, 9, 6, 8, 5, 10, 4, 3, 7, 1],
            [2, 10, 8, 6, 4, 9, 5, 1, 7, 3],
            [6, 7, 8, 9, 10, 3, 5, 2, 4, 1],
            [6, 10, 9, 8, 7, 5, 3, 1, 4, 2],
        ]
        ngons = generate_ngons(5)
        for correct_ngon in correct_5_gons:
            self.assertIn(correct_ngon, ngons)
    
    def test_calculate_ngon_str_3(self):
        self.assertEqual(calculate_ngon_str([1, 2, 3, 5, 6, 4]), '156264345')
    
    def test_calculate_ngon_str_4(self):
        self.assertEqual(calculate_ngon_str([1, 2, 3, 4, 5, 8, 10, 7, 9, 6]),
                         '18102107379496568')

    def test_result_3(self):
        self.assertEqual(p68(3, 9), 432621513)

    def test_result_5(self):
        self.assertEqual(p68(5, 16), 6531031914842725)
