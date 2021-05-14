import unittest

from hedger import utils


class CsvTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_filepath = 'tests/data/temp.csv'

    def tearDown(self) -> None:
        if utils.path_exists(self.temp_filepath):
            utils.remove(self.temp_filepath)

    def assertCsvEqual(self, first_filepath, second_filepath):
        self._assert_csv_row_count_equal(first_filepath, second_filepath)

        with utils.CsvReader(first_filepath) as first_reader, \
                utils.CsvReader(second_filepath)as second_reader:

            for first_line, second_line in zip(first_reader, second_reader):
                self.assertDictEqual(first_line, second_line)

    def assertCsvAlmostEqual(
            self,
            first_filepath,
            second_filepath,
            places=None
    ):
        self._assert_csv_row_count_equal(first_filepath, second_filepath)

        with utils.CsvReader(first_filepath) as first_reader, \
                utils.CsvReader(second_filepath)as second_reader:

            for first_line, second_line in zip(first_reader, second_reader):
                self._assert_dicts_almost_equal(
                    first_line,
                    second_line,
                    places
                )

    def _assert_dicts_almost_equal(self, first_line, second_line, places):
        self._assert_keys_equal(first_line, second_line)
        for k, first_value in first_line.items():
            second_value = second_line[k]
            if utils.isfloat(first_value) or utils.isfloat(second_value):
                self.assertAlmostEqual(
                    first_value,
                    second_value,
                    places=places
                )
            else:
                self.assertEqual(first_value, second_value)

    def _assert_keys_equal(self, first_line, second_line):
        self.assertListEqual(list(first_line.keys()), list(second_line.keys()))

    def _assert_csv_row_count_equal(self, first_filepath, second_filepath):
        with utils.CsvReader(first_filepath) as first_reader, \
                utils.CsvReader(second_filepath)as second_reader:
            first_rows = self._count_csv_rows(first_reader)
            second_rows = self._count_csv_rows(second_reader)

            self.assertEqual(first_rows, second_rows)

    def _count_csv_rows(self, reader):
        return len(list(reader))
