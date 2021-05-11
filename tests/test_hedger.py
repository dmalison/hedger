import unittest

import hedger
from tests import utils as tests_utils


class HedgerTest(unittest.TestCase):
    def setUp(self):
        self.csv_filepath = 'tests/data/temp.csv'

    def tearDown(self) -> None:
        if tests_utils.path_exists(self.csv_filepath):
            tests_utils.remove(self.csv_filepath)

    def test_generate_score_csv_with_four_teams(self):
        teams = ['Gonzaga', 'Michigan', 'Baylor', 'Illinois']
        actual_filepath = "tests/data/bracket_scores.csv"
        hedger.generate_score_csv(teams, filepath=actual_filepath)

        fixture_filepath = "tests/data/test_generate_score_csv_fixture.csv"

        # tests_utils.assert_csv_equal(actual_filepath, fixture_filepath)
