import unittest

from tests import utils


class UtilsTest(unittest.TestCase):
    def test_assert_csv_equal_on_two_equal_csvs(self):
        first = 'tests/data/test_assert_csv_first_fixture.csv'
        second = 'tests/data/test_assert_csv_second_fixture.csv'
        utils.assert_csv_equal(first, second)

    def test_assert_csv_equal_different_row_counts(self):
        first = 'tests/data/test_assert_csv_first_fixture.csv'
        second = 'tests/data/test_assert_csv_row_count_fixture.csv'
        with self.assertRaises(AssertionError):
            utils.assert_csv_equal(first, second)

    def test_assert_csv_equal_different_values(self):
        first = 'tests/data/test_assert_csv_first_fixture.csv'
        second = 'tests/data/test_assert_csv_values_fixture.csv'
        with self.assertRaises(AssertionError):
            utils.assert_csv_equal(first, second)
