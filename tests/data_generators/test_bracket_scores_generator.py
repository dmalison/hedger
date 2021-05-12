import unittest

from hedger import csv_generators
from tests import utils as tests_utils


class BracketScoresGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.csv_filepath = 'tests/data/temp.csv'

    def tearDown(self) -> None:
        if tests_utils.path_exists(self.csv_filepath):
            tests_utils.remove(self.csv_filepath)

    def test_generate_scores_csv_with_four_teams(self):
        teams = ['Gonzaga', 'Michigan', 'Baylor', 'Illinois']
        scores_generator = csv_generators.ScoresGenerator(teams)
        scores_generator.write(self.csv_filepath)

        fixture_filepath = "tests/data/test_generate_scores_csv_fixture.csv"
        tests_utils.assert_csv_equal(self.csv_filepath, fixture_filepath)
