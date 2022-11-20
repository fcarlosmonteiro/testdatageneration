from unittest import TestCase
from target.uri_2221 import func


class URI2221Test(TestCase):

    def test_func(self):
        self.assertEqual(func(5, 12, 23, 15, 42, 12, 20), "Guarte")