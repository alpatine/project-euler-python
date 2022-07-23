from fractions import Fraction
from re import L
from unittest import TestCase, expectedFailure
from farey import calculate_mediant, farey_sequence, farey_sequence_length, term_left_of

class Calculate_Mediant_Test(TestCase):
    def test_1_2_3_4(self):
        left = Fraction(1, 2)
        right = Fraction(3, 4)
        expected = Fraction(2, 3)
        self.assertEqual(calculate_mediant(left, right), expected)

class Farey_Sequence_Test(TestCase):
    def test_1(self):
        expected = [
            Fraction(0, 1),
            Fraction(1, 1),
        ]
        result = list(farey_sequence(1))
        self.assertEqual(result, expected)
    
    def test_2(self):
        expected = [
            Fraction(0, 1),
            Fraction(1, 2),
            Fraction(1, 1),
        ]
        result = list(farey_sequence(2))
        self.assertEqual(result, expected)
    
    def test_5(self):
        expected = [
            Fraction(0, 1),
            Fraction(1, 5),
            Fraction(1, 4),
            Fraction(1, 3),
            Fraction(2, 5),
            Fraction(1, 2),
            Fraction(3, 5),
            Fraction(2, 3),
            Fraction(3, 4),
            Fraction(4, 5),
            Fraction(1, 1),
        ]
        result = list(farey_sequence(5))
        self.assertEqual(result, expected)

class Farey_Sequence_Length_Test(TestCase):
    def test_1(self):
        self.assertEqual(farey_sequence_length(1), 2)
    
    def test_2(self):
        self.assertEqual(farey_sequence_length(2), 3)
    
    def test_8(self):
        self.assertEqual(farey_sequence_length(8), 23)

class Term_Left_Of_Test(TestCase):
    def test_8_3_7(self):
        n = 8
        target = Fraction(3, 7)
        expected = Fraction(2, 5)
        result = term_left_of(n, target)
        self.assertEqual(result, expected)
    
    def test_5_3_4(self):
        n = 5
        target = Fraction(3, 4)
        expected = Fraction(2, 3)
        result = term_left_of(n, target)
        self.assertEqual(result, expected)

    def test_1000000_3_7(self):
        n = 1000000
        target = Fraction(3, 7)
        expected = Fraction(428570, 999997)
        result = term_left_of(n, target)
        self.assertEqual(result, expected)
