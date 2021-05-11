import unittest

from hedger import utils


class CsvReaderTest(unittest.TestCase):
    def test_read_test_fixture(self):
        fixture_filepath = 'tests/data/test_csv_reader_fixture.csv'
        expected = [
            {'col1': 'A', 'col2': '1'},
            {'col1': 'B', 'col2': '2'}
        ]

        with utils.CsvReader(fixture_filepath) as reader:
            self.assertListEqual(expected, list(reader))
