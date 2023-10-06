from tkinter import N
from unittest import TestCase
from p46 import p46

class P46_Test(TestCase):
    def test_34(self):
        self.assertEqual(p46(34), None)
    
    def test_answer(self):
        self.assertEqual(p46(5778), 5777)