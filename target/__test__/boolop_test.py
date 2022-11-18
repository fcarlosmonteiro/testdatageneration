from unittest import TestCase
from boolop import boolop_test


class BoolopTest(TestCase):

    def test_boolop_test(self):
        self.assertEqual(boolop_test(765), 3)
