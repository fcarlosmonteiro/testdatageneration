from unittest import TestCase
from target.uri_2139 import func


class URI2139Test(TestCase):

    def test_func(self):
        self.assertEqual(func(12, 25), "E natal!")