from unittest import TestCase
from p51 import p51

class P51_Test(TestCase):
    def test_result(self):
        self.assertEqual(p51(1000000), 121313)
