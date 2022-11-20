from unittest import TestCase
from target.uri_2812 import func


class URI2812Test(TestCase):

    def test_func(self):
        self.assertEqual(func(10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), '9 1 7 3 5')