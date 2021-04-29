import unittest

import hedger
from hedger import Result


class BracketTest(unittest.TestCase):
    def setUp(self):
        gryffindor = hedger.Entry('Gryffindor')
        slytherin = hedger.Entry('Slytherin')
        ravenclaw = hedger.Entry('Ravenclaw')
        hufflepuff = hedger.Entry('Hufflepuff')
        entries = [
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

        self.tournament = hedger.Tournament(entries)
        self.bracket = self.tournament._make_bracket(self.results)

    def test_compute_score_with_correct_bracket(self):
        scoring_bracket = self.tournament._make_bracket(self.results)

        actual = self.bracket.compute_score(scoring_bracket)
        expected = 640

        self.assertEqual(actual, expected)

    def test_compute_score_with_incorrect_bracket(self):
        scoring_bracket = self.tournament._make_bracket(
            [Result.BOTTOM_WINS, Result.TOP_WINS, Result.TOP_WINS]
        )

        actual = self.bracket.compute_score(scoring_bracket)
        expected = 0

        self.assertEqual(actual, expected)

    def test_compute_score_with_partially_correct_bracket(self):
        scoring_bracket = self.tournament._make_bracket(
            [Result.TOP_WINS, Result.TOP_WINS, Result.TOP_WINS]
        )

        actual = self.bracket.compute_score(scoring_bracket)
        expected = 480

        self.assertEqual(actual, expected)
