from unittest import TestCase
from p61 import bucket_numbers, extend_cycle, p61

class P61_Test(TestCase):
    def test_result(self):
        self.assertEquals(p61(), 28684)
    
    def test_bucket_numbers(self):
        source = range(1111, 2111, 75)
        expected = {
            '11': ['11', '86'],
            '12': ['61'],
            '13': ['36'],
            '14': ['11', '86'],
            '15': ['61'],
            '16': ['36'],
            '17': ['11', '86'],
            '18': ['61'],
            '19': ['36'],
            '20': ['11', '86'],
        }
        self.assertEqual(bucket_numbers(source), expected)
    
    def test_extend_cycle(self):
        root = '11'
        head = '15'
        figurate_numbers = [
            {
                '11': ['11', '12'],
                '12': ['13', '14'],
                '17': ['11', '16'],
            },
            {},
            {
                '11': ['21', '22'],
                '15': ['13', '17']
            }
        ]
        figures_included = [1]
        expected = ['1517', '1711']
        self.assertEqual(
            extend_cycle(root,
                         head,
                         figurate_numbers,
                         figures_included),
            expected)
