from hedger import writers
from tests import utils as tests_utils


class ScoresGeneratorTest(tests_utils.CsvTestCase):
    def test_generate_scores_csv_with_four_teams(self):
        teams = [
            {'name': 'Gonzaga'},
            {'name': 'Michigan'},
            {'name': 'Baylor'},
            {'name': 'Illinois'}
        ]

        scores_generator = writers.ScoresWriter(teams)
        scores_generator._path = self.temp_path
        scores_generator.write()

        fixture_path = "tests/data/test_generate_scores_csv_fixture.csv"
        self.assertCsvEqual(self.temp_path, fixture_path)
