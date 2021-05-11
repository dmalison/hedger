import unittest

from hedger import utils
from tests import utils as tests_utils


class CsvWriterTest(unittest.TestCase):
    def setUp(self):
        self.csv_filepath = 'tests/data/temp.csv'

    def tearDown(self) -> None:
        if tests_utils.path_exists(self.csv_filepath):
            tests_utils.remove(self.csv_filepath)

    def test_write_lines_and_check_against_fixture(self):
        with utils.CsvWriter(self.csv_filepath, ['col1', 'col2']) as writer:
            writer.writerow({'col1': 'A', 'col2': 1})
            writer.writerow({'col1': 'B', 'col2': 2})

        fixture_filepath = 'tests/data/test_csv_writer_fixture.csv'
        tests_utils.assert_csv_equal(self.csv_filepath, fixture_filepath)

    def test_write_wrong_line_and_raise_error(self):
        with utils.CsvWriter(self.csv_filepath, ['col1', 'col2']) as writer:
            writer.writerow({'col1': 'C', 'col2': 3})

        fixture_filepath = 'tests/data/test_csv_writer_fixture.csv'
        with self.assertRaises(AssertionError):
            tests_utils.assert_csv_equal(self.csv_filepath, fixture_filepath)
