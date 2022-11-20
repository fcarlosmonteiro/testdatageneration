from unittest import TestCase
from target.uri_2059 import func


class URI2059Test(TestCase):

    def test_func(self):
        self.assertEqual(func(1, 4, 5, 0, 0), 'Jogador 2 ganha!')