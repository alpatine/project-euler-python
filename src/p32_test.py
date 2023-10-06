from unittest import TestCase
from p32 import find_pandigital, p32

class P32_Test(TestCase):

    def test_example(self):
        self.assertEqual(find_pandigital(39, 40, 186, 187, 1234, 9876), {7254})

    def test_p32(self):
        self.assertEqual(p32(), 45228)
