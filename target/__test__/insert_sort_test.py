from unittest import TestCase
from insert_sort import insert_sort


class InsertSortTest(TestCase):

    def test_orelse(self):
        self.assertEqual(insert_sort(52, 46, 2, 7584, 542), [2.0, 46.0, 52.0, 542.0, 7584.0])