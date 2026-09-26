from unittest import TestCase

from p89 import DATA_FILE_PATH, load_data, p89


class p89_Test(TestCase):
    def test_example_XIIIIII(self):
        self.assertEqual(p89(['XIIIIII']), 4)

    def test_XXXXVIIII(self):
        # len('XXXXVIIII') = 9
        # len('XLIX') = 4
        self.assertEqual(p89(['XXXXVIIII']), 5)

    def test_solution(self):
        problem_data = load_data(DATA_FILE_PATH)
        self.assertEqual(p89(problem_data), 743)
