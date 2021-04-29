import unittest

import hedger
from hedger import Result


class BracketTest(unittest.TestCase):
    def setUp(self):
        gryffindor = hedger.Entry('Gryffindor')
        slytherin = hedger.Entry('Slytherin')
        ravenclaw = hedger.Entry('Ravenclaw')
        hufflepuff = hedger.Entry('Hufflepuff')
        self.entries = [
            gryffindor,
            ravenclaw,
            hufflepuff,
            slytherin
        ]
        self.results = [
            Result.TOP_WINS,
            Result.BOTTOM_WINS,
            Result.TOP_WINS
        ]

        bracket_builder = hedger.BracketBuilder(self.entries, self.results)
        self.bracket = bracket_builder.get_bracket()

    def test_compute_score_with_correct_bracket(self):
        scoring_bracket = self.bracket

        actual = self.bracket.compute_score(scoring_bracket)
        expected = 640

        self.assertEqual(actual, expected)

    def test_compute_score_with_incorrect_bracket(self):
        new_results = [Result.BOTTOM_WINS, Result.TOP_WINS, Result.TOP_WINS]
        bracket_builder = hedger.BracketBuilder(self.entries, new_results)
        scoring_bracket = bracket_builder.get_bracket()

        actual = self.bracket.compute_score(scoring_bracket)
        expected = 0

        self.assertEqual(actual, expected)

    def test_compute_score_with_partially_correct_bracket(self):
        new_results = [Result.TOP_WINS, Result.TOP_WINS, Result.TOP_WINS]
        bracket_builder = hedger.BracketBuilder(self.entries, new_results)
        scoring_bracket = bracket_builder.get_bracket()

        actual = self.bracket.compute_score(scoring_bracket)
        expected = 480

        self.assertEqual(actual, expected)
