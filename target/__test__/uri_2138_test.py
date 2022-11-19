from unittest import TestCase
from target.uri_2138 import func


class URI2138Test(TestCase):

    def test_func(self):
        self.assertEqual(func('3981152060'), 1)