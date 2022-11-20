from unittest import TestCase
from target.uri_1847 import func


class URI1847Test(TestCase):

    def test_func(self):
        self.assertEqual(func(20, 10, 12), ':)')