from hedger import csv_generators
from tests import utils as tests_utils


class ScoresGeneratorTest(tests_utils.CsvTestCase):
    def test_generate_scores_csv_with_four_teams(self):
        teams = [
            {'name': 'Gonzaga'},
            {'name': 'Michigan'},
            {'name': 'Baylor'},
            {'name': 'Illinois'}
        ]

        scores_generator = csv_generators.ScoresGenerator(teams)
        scores_generator.write(self.temp_filepath)

        fixture_filepath = "tests/data/test_generate_scores_csv_fixture.csv"
        self.assertCsvEqual(self.temp_filepath, fixture_filepath)
