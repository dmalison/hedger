import unittest

import hedger
from hedger import Result, utils


class BracketTest(unittest.TestCase):
    def setUp(self):
        teams = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
        entries = [hedger.Entry(team, rating=100) for team in teams]
        equal_tournament = hedger.Tournament(entries)

        gryffindor = hedger.Entry('Gryffindor', rating=106.264)
        slytherin = hedger.Entry('Slytherin', rating=93.736)
        ravenclaw = hedger.Entry('Ravenclaw', rating=100)
        hufflepuff = hedger.Entry('Hufflepuff', rating=100)
        entries = [gryffindor, ravenclaw, hufflepuff, slytherin]
        unequal_tournament = hedger.Tournament(entries)

        self.results = [
            Result.TOP_WINS,
            Result.BOTTOM_WINS,
            Result.TOP_WINS
        ]
        bracket_builder = hedger.BracketBuilder(
            equal_tournament,
            self.results
        )
        self.equal_bracket = bracket_builder.get_bracket()
        bracket_builder = hedger.BracketBuilder(
            unequal_tournament,
            self.results
        )
        self.unequal_bracket = bracket_builder.get_bracket()

    def test_code_with_four_teams(self):
        expected = 5
        actual = self.equal_bracket.code
        self.assertEqual(expected, actual)

    def test_prob_with_four_teams_with_equal_ratings(self):
        expected = .125
        actual = self.equal_bracket.prob
        self.assertEqual(actual, expected)

    def test_prob_with_four_teams_with_unequal_ratings(self):
        expected = .169

        actual = self.unequal_bracket.prob
        self.assertAlmostEqual(actual, expected, 3)

    def test_make_dist_with_four_equal_teams(self):
        expected = [
            utils.Point(omega=2, prob=.125, value=0),
            utils.Point(omega=3, prob=.125, value=0),
            utils.Point(omega=0, prob=.125, value=160),
            utils.Point(omega=1, prob=.125, value=160),
            utils.Point(omega=6, prob=.125, value=160),
            utils.Point(omega=4, prob=.125, value=320),
            utils.Point(omega=7, prob=.125, value=480),
            utils.Point(omega=5, prob=.125, value=640)
        ]
        actual = self.equal_bracket.dist._points

        self.assertEqual(actual, expected)

    def test_make_dist_with_four_unequal_teams(self):
        expected = [
            utils.Point(omega=2, prob=.09375, value=0),
            utils.Point(omega=3, prob=.09375, value=0),
            utils.Point(omega=0, prob=.01563, value=160),
            utils.Point(omega=1, prob=.04688, value=160),
            utils.Point(omega=6, prob=.14062, value=160),
            utils.Point(omega=4, prob=.01875, value=320),
            utils.Point(omega=7, prob=.42188, value=480),
            utils.Point(omega=5, prob=.16875, value=640)
        ]
        actual = self.unequal_bracket.dist._points

        for actual_point, expected_point in zip(actual, expected):
            self.assertEqual(actual_point.omega, expected_point.omega)
            self.assertEqual(actual_point.value, expected_point.value)
            self.assertAlmostEqual(actual_point.prob, expected_point.prob, 4)

    def test_summarize_with_four_equal_teams(self):
        expected = utils.Summary(mean=240, p10=0, p90=640)
        actual = self.equal_bracket.summarize()
        self.assertEqual(actual, expected)

    def test_summarize_with_four_unequal_teams(self):
        expected = utils.Summary(mean=349, p10=0, p90=640)
        actual = self.unequal_bracket.summarize()
        self.assertEqual(actual.p10, expected.p10)
        self.assertEqual(actual.p90, expected.p90)
        self.assertAlmostEqual(actual.mean, expected.mean, 1)
