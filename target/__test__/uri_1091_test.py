from unittest import TestCase
from target.uri_1091 import func


class URI1091Test(TestCase):

    def test_func(self):
        self.assertEqual(func(2, 1, 10, 10), 'NE')