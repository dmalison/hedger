import unittest

from hedger import utils
from tests import utils as tests_utils


class CsvReaderTest(unittest.TestCase):
    def test_read_test_fixture(self):
        fixture_path = 'tests/data/test_csv_reader_fixture.csv'
        expected = [
            {'col1': 'A', 'col2': 1, 'col3': .1},
            {'col1': 'B', 'col2': 2, 'col3': .2}
        ]

        with utils.CsvReader(fixture_path, ('col1', 'col2', 'col3')) as reader:
            self.assertListEqual(expected, reader.read_all())


class CsvWriterTest(tests_utils.CsvTestCase):
    def test_write_lines_and_check_against_fixture(self):
        with utils.CsvWriter(self.temp_path, ['col1', 'col2']) as writer:
            writer.writerow({'col1': 'A', 'col2': 1})
            writer.writerow({'col1': 'B', 'col2': 2})

        fixture_path = 'tests/data/test_csv_writer_fixture.csv'
        self.assertCsvEqual(self.temp_path, fixture_path)

    def test_write_wrong_line_and_raise_error(self):
        with utils.CsvWriter(self.temp_path, ['col1', 'col2']) as writer:
            writer.writerow({'col1': 'C', 'col2': 3})

        fixture_path = 'tests/data/test_csv_writer_fixture.csv'
        with self.assertRaises(AssertionError):
            self.assertCsvEqual(self.temp_path, fixture_path)
