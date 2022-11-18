from unittest import TestCase
from target.uri_2060 import func


class URI2060Test(TestCase):

    def test_func(self):
        self.assertEqual(func(2, 5, 4, 20, 10), "4 Multiplo(s) de 2, 0 Multiplo(s) de 3, 2 Multiplo(s) de 4 e 3 Multiplo(s) de 5")