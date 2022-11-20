from unittest import TestCase
from target.uri_2140 import func


class URI2140Test(TestCase):

    def test_func(self):
        self.assertEqual(func(11, 23), "possible")