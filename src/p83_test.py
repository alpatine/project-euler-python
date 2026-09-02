from unittest import TestCase

from p83 import DATA_FILE_PATH, load_data, p83


class P83_Test(TestCase):
    def test_example(self):
        test_matrix = [
            [ 131, 673, 234, 103, 18 ],
            [ 201, 96, 342, 965, 150 ],
            [ 630, 803, 746, 422, 111 ],
            [ 537, 699, 497, 121, 956 ],
            [ 805, 732, 524, 37, 331 ],
        ]
        self.assertEqual(p83(test_matrix), 2297)

    def test_solution(self):
        matrix = load_data(DATA_FILE_PATH)
        self.assertEqual(p83(matrix), 425185)
