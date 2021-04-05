from unittest import TestCase
from p33 import can_digit_cancel, p33

class P33_Test(TestCase):
    def test_p33(self):
        self.assertEqual(p33(), 100)

class Can_Digit_Cancel_Test(TestCase):
    def test_trivial(self):
        self.assertEqual(can_digit_cancel(30, 50), False)
    
    def test_49_98(self):
        self.assertEqual(can_digit_cancel(49, 98), True)