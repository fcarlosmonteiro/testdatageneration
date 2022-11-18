from unittest import TestCase
from target.fizzbuzz import generate_fizzbuzz


class FizzbuzzTest(TestCase):

    def test_generate_fizzbuzz(self):
        self.assertNotEquals(generate_fizzbuzz(15), '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz')