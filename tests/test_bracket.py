import unittest

import hedger
from hedger.result import Result


class BracketTest(unittest.TestCase):
    def test_score_against_two_teams_with_correct_bracket(self):
        gryffindor = hedger.Entry('Gryffindor')
        slytherin = hedger.Entry('Slytherin')
        entries = [gryffindor, slytherin]
        quidditch_cup = hedger.Tournament(entries)
        bracket = quidditch_cup.make_bracket([Result.TOP_WINS])
        scoring_bracket = quidditch_cup.make_bracket([Result.TOP_WINS])

        actual = bracket.score_against(scoring_bracket)
        expected = 320

        self.assertEqual(actual, expected)

    def test_score_against_two_teams_with_incorrect_bracket(self):
        gryffindor = hedger.Entry('Gryffindor')
        slytherin = hedger.Entry('Slytherin')
        entries = [gryffindor, slytherin]
        quidditch_cup = hedger.Tournament(entries)
        bracket = quidditch_cup.make_bracket([Result.TOP_WINS])
        scoring_bracket = quidditch_cup.make_bracket([Result.BOTTOM_WINS])

        actual = bracket.score_against(scoring_bracket)
        expected = 0

        self.assertEqual(actual, expected)
