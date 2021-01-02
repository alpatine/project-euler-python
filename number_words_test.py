from unittest import TestCase
from number_words import number_to_words

class Number_Words_Test(TestCase):
    def test_ones(self):
        self.assertEqual(number_to_words(1), 'one')
        self.assertEqual(number_to_words(2), 'two')
        self.assertEqual(number_to_words(3), 'three')
        self.assertEqual(number_to_words(4), 'four')
        self.assertEqual(number_to_words(5), 'five')
        self.assertEqual(number_to_words(6), 'six')
        self.assertEqual(number_to_words(7), 'seven')
        self.assertEqual(number_to_words(8), 'eight')
        self.assertEqual(number_to_words(9), 'nine')
    
    def test_tens(self):
        self.assertEqual(number_to_words(10), 'ten')
        self.assertEqual(number_to_words(20), 'twenty')
        self.assertEqual(number_to_words(30), 'thirty')
        self.assertEqual(number_to_words(40), 'forty')
        self.assertEqual(number_to_words(50), 'fifty')
        self.assertEqual(number_to_words(60), 'sixty')
        self.assertEqual(number_to_words(70), 'seventy')
        self.assertEqual(number_to_words(80), 'eighty')
        self.assertEqual(number_to_words(90), 'ninety')
    
    def test_teens(self):
        self.assertEqual(number_to_words(11), 'eleven')
        self.assertEqual(number_to_words(12), 'twelve')
        self.assertEqual(number_to_words(13), 'thirteen')
        self.assertEqual(number_to_words(14), 'fourteen')
        self.assertEqual(number_to_words(15), 'fifteen')
        self.assertEqual(number_to_words(16), 'sixteen')
        self.assertEqual(number_to_words(17), 'seventeen')
        self.assertEqual(number_to_words(18), 'eighteen')
        self.assertEqual(number_to_words(19), 'nineteen')

    def test_hundreds(self):
        self.assertEqual(number_to_words(100), 'onehundred')
        self.assertEqual(number_to_words(200), 'twohundred')
        self.assertEqual(number_to_words(300), 'threehundred')
        self.assertEqual(number_to_words(400), 'fourhundred')
        self.assertEqual(number_to_words(500), 'fivehundred')
        self.assertEqual(number_to_words(600), 'sixhundred')
        self.assertEqual(number_to_words(700), 'sevenhundred')
        self.assertEqual(number_to_words(800), 'eighthundred')
        self.assertEqual(number_to_words(900), 'ninehundred')
    
    def test_scales(self):
        self.assertEqual(number_to_words(1000), 'onethousand')
        self.assertEqual(number_to_words(1000000), 'onemillion')
    
    def test_combos(self):
        self.assertEqual(number_to_words(27), 'twentyseven')
        self.assertEqual(number_to_words(507), 'fivehundredandseven')
        self.assertEqual(number_to_words(314), 'threehundredandfourteen')
        self.assertEqual(number_to_words(825), 'eighthundredandtwentyfive')
