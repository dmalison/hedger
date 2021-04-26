import unittest

import hedger
from hedger.result import Result


class BracketTest(unittest.TestCase):
    def setUp(self):
        self.gryffindor = hedger.Entry('Gryffindor')
        self.slytherin = hedger.Entry('Slytherin')
        self.entries = [self.gryffindor, self.slytherin]
        self.tournament = hedger.Tournament(self.entries)
        self.bracket = self.tournament.make_bracket([Result.TOP_WINS])

    def test_score_against_two_teams_with_correct_bracket(self):
        scoring_bracket = self.tournament.make_bracket([Result.TOP_WINS])

        actual = self.bracket.score_against(scoring_bracket)
        expected = 320

        self.assertEqual(actual, expected)

    def test_score_against_two_teams_with_incorrect_bracket(self):
        scoring_bracket = self.tournament.make_bracket([Result.BOTTOM_WINS])

        actual = self.bracket.score_against(scoring_bracket)
        expected = 0

        self.assertEqual(actual, expected)
