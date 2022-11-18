from unittest import TestCase
from target.uri_2702 import func


class URI2702Test(TestCase):

    def test_func(self):
        self.assertEqual(func(80, 20, 40, 45, 23, 48), 11)