from unittest import TestCase
from target.selection_sort import selection_sort


class SelectionSortTest(TestCase):

    def test_selection_sort(self):
        self.assertEqual(selection_sort(52, 46, 2, 7584, 542), [2.0, 46.0, 52.0, 542.0, 7584.0])