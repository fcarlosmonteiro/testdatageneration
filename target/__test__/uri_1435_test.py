from unittest import TestCase
from target.uri_1435 import func


class URI1435Test(TestCase):

    def test_func(self):
        self.assertNotEqual(func(5), '1 1')