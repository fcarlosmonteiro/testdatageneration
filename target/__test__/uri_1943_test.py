from unittest import TestCase
from target.uri_1943 import func


class URI1943Test(TestCase):

    def test_func(self):
        self.assertEqual(func(7), "Top 10")