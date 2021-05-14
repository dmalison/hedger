import unittest

import hedger
from hedger import Result


class BracketTest(unittest.TestCase):
    def setUp(self):
        gryffindor = hedger.Entry('Gryffindor', rating=100)
        slytherin = hedger.Entry('Slytherin', rating=100)
        ravenclaw = hedger.Entry('Ravenclaw', rating=100)
        hufflepuff = hedger.Entry('Hufflepuff', rating=100)
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

        actual = self.bracket.get_score(scoring_bracket)
        expected = 640

        self.assertEqual(actual, expected)

    def test_compute_score_with_incorrect_bracket(self):
        new_results = [Result.BOTTOM_WINS, Result.TOP_WINS, Result.TOP_WINS]
        bracket_builder = hedger.BracketBuilder(self.entries, new_results)
        scoring_bracket = bracket_builder.get_bracket()

        actual = self.bracket.get_score(scoring_bracket)
        expected = 0

        self.assertEqual(actual, expected)

    def test_compute_score_with_partially_correct_bracket(self):
        new_results = [Result.TOP_WINS, Result.TOP_WINS, Result.TOP_WINS]
        bracket_builder = hedger.BracketBuilder(self.entries, new_results)
        scoring_bracket = bracket_builder.get_bracket()

        actual = self.bracket.get_score(scoring_bracket)
        expected = 480

        self.assertEqual(actual, expected)

    def test_get_code_with_four_teams(self):
        expected = 5
        actual = self.bracket.get_code()
        self.assertEqual(expected, actual)

    def test_get_prob_with_four_teams_with_equal_ratings(self):
        expected = .125
        actual = self.bracket.get_prob()
        self.assertEqual(actual, expected)

    def test_get_prob_with_four_teams_with_unequal_ratings(self):
        expected = .169

        gryffindor = hedger.Entry('Gryffindor', rating=106.264)
        slytherin = hedger.Entry('Slytherin', rating=93.736)
        ravenclaw = hedger.Entry('Ravenclaw', rating=100)
        hufflepuff = hedger.Entry('Hufflepuff', rating=100)

        entries = [gryffindor, ravenclaw, hufflepuff, slytherin]
        bracket_builder = hedger.BracketBuilder(entries, self.results)
        bracket = bracket_builder.get_bracket()

        actual = bracket.get_prob()
        self.assertAlmostEqual(actual, expected, 3)
