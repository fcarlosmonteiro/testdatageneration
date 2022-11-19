from unittest import TestCase
from target.uri_1131 import func


class URI1131Test(TestCase):

    def test_func(self):
        self.assertEqual(func(3, 2), '1 grenais\nInter: 1\nGremio: 0\nEmpates: 0\nInter venceu mais')