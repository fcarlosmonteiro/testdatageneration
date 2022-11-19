from unittest import TestCase
from target.uri_2028 import func


class URI2028Test(TestCase):

    def test_func(self):
        self.assertEqual(func(3), "7 numero\n0 1 2 2 3 3 3")