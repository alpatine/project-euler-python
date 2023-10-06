from unittest import TestCase
from p38 import p38, calculate_concatenated_product

class P38_Test(TestCase):
    def test_concat_product_192_3(self):
        self.assertEqual(calculate_concatenated_product(192, 4), 192384576)
    
    def test_concat_product_9_6(self):
        self.assertEqual(calculate_concatenated_product(9, 6), 918273645)

    def test_p38_correct_answer(self):
        self.assertEqual(p38(), 932718654)