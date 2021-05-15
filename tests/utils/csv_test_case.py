import unittest

from hedger import utils


class CsvTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_path = 'tests/data/temp.csv'

    def tearDown(self) -> None:
        if utils.path_exists(self.temp_path):
            utils.remove(self.temp_path)

    def assertCsvEqual(self, first_path, second_path):
        self._assert_csv_row_count_equal(first_path, second_path)

        with utils.CsvReader(first_path) as first_reader, \
                utils.CsvReader(second_path)as second_reader:

            for first_line, second_line in zip(first_reader, second_reader):
                self.assertDictEqual(first_line, second_line)

    def assertCsvAlmostEqual(self, first_path, second_path, places=None):
        self._assert_csv_row_count_equal(first_path, second_path)

        with utils.CsvReader(first_path) as first_reader, \
                utils.CsvReader(second_path)as second_reader:

            for first_line, second_line in zip(first_reader, second_reader):
                self._assert_dicts_almost_equal(
                    first_line,
                    second_line,
                    places
                )

    def _assert_dicts_almost_equal(self, first_line, second_line, places):
        self._assert_keys_equal(first_line, second_line)
        for k, first_v in first_line.items():
            second_v = second_line[k]
            if isinstance(first_v, float) and isinstance(second_v, float):
                self.assertAlmostEqual(
                    first_v,
                    second_v,
                    places=places
                )
            else:
                self.assertEqual(first_v, second_v)

    def _assert_keys_equal(self, first_line, second_line):
        self.assertListEqual(list(first_line.keys()), list(second_line.keys()))

    def _assert_csv_row_count_equal(self, first_path, second_path):
        with utils.CsvReader(first_path) as first_reader, \
                utils.CsvReader(second_path)as second_reader:
            first_rows = self._count_csv_rows(first_reader)
            second_rows = self._count_csv_rows(second_reader)

            self.assertEqual(first_rows, second_rows)

    def _count_csv_rows(self, reader):
        return len(list(reader))
