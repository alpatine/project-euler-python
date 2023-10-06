from unittest import TestCase
from collatz import collatz_length, reset_cached_lengths, collatz_lengths

class Collatz_Test(TestCase):

    def test_1(self):
        self.assertEqual(collatz_length(1), 1)

    def test_13(self):
        self.assertEqual(collatz_length(13), 10)

    def test_reset(self):
        collatz_length(1)
        reset_cached_lengths()
        self.assertEqual(collatz_lengths, {})
    
    def test_cache(self):
        reset_cached_lengths()
        collatz_length(4)
        self.assertEqual(collatz_length(16), 5)

