from unittest import TestCase
from target.uri_1179 import func


class URI1179Test(TestCase):

    def test_func(self):
        self.assertNotEqual(func(1, 3, 4, -4, 2, 3, 8, 2, 5, -7, 54, 76, 789, 23, 98), 'Q')