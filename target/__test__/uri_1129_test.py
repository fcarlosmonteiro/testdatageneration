from unittest import TestCase
from target.uri_1129 import func


class URI1129Test(TestCase):

    def test_func(self):
        self.assertEqual(func(0, 255, 255, 255, 255), "A")