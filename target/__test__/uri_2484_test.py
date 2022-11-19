from unittest import TestCase
from target.uri_2484 import func


class URI2484Test(TestCase):

    def test_func(self):
        self.assertNotEqual(func(400.00), '5')