import unittest
from pythagoras import calculate_next_triplets

class Pythagoras_Test(unittest.TestCase):
    def test_calculate_next_triplets_3_4_5(self):
        expected_result = ((5, 12, 13), (21, 20, 29), (15, 8, 17))
        self.assertEqual(calculate_next_triplets((3, 4, 5)), expected_result)

    def test_calculate_next_triplets_5_12_13(self):
        expected_result = ((7, 24, 25), (55, 48, 73), (45, 28, 53))
        self.assertEqual(calculate_next_triplets((5, 12, 13)), expected_result)