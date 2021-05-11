import unittest

from hedger import utils


def assert_csv_equal(first_filepath: str, second_filepath: str):
    with utils.CsvReader(first_filepath) as first_reader, \
            utils.CsvReader(second_filepath)as second_reader:

        _assert_csv_row_count_equal(first_filepath, second_filepath)

        test_case = unittest.TestCase()
        for first_line, second_line in zip(first_reader, second_reader):
            test_case.assertDictEqual(first_line, second_line)


def _assert_csv_row_count_equal(first_filepath, second_filepath):
    with utils.CsvReader(first_filepath) as first_reader, \
            utils.CsvReader(second_filepath)as second_reader:
        first_rows = _count_csv_rows(first_reader)
        second_rows = _count_csv_rows(second_reader)

        test_case = unittest.TestCase()
        test_case.assertEqual(first_rows, second_rows)


def _count_csv_rows(reader):
    return len(list(reader))
