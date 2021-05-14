from hedger import utils
from tests import utils as tests_utils


class CsvWriterTest(tests_utils.CsvTestCase):
    def test_write_lines_and_check_against_fixture(self):
        with utils.CsvWriter(self.temp_filepath, ['col1', 'col2']) as writer:
            writer.writerow({'col1': 'A', 'col2': 1})
            writer.writerow({'col1': 'B', 'col2': 2})

        fixture_filepath = 'tests/data/test_csv_writer_fixture.csv'
        self.assertCsvEqual(self.temp_filepath, fixture_filepath)

    def test_write_wrong_line_and_raise_error(self):
        with utils.CsvWriter(self.temp_filepath, ['col1', 'col2']) as writer:
            writer.writerow({'col1': 'C', 'col2': 3})

        fixture_filepath = 'tests/data/test_csv_writer_fixture.csv'
        with self.assertRaises(AssertionError):
            self.assertCsvEqual(self.temp_filepath, fixture_filepath)