from unittest import TestCase
from target.uri_1132 import func


class SelectionSortTest(TestCase):

    def test_func(self):
        self.assertEqual(func(52, 46), 291)