from unittest import TestCase
from p37 import p37

class P37_Test(TestCase):
    def test_correct_answer(self):
        self.assertEqual(p37(), 748317)
