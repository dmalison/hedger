import unittest

import hedger
from hedger import Result


class MatchTest(unittest.TestCase):
    def setUp(self):
        self.entry_a = hedger.Entry('A')
        self.entry_b = hedger.Entry('B')
        self.entry_c = hedger.Entry('C')
        self.entry_d = hedger.Entry('D')
        self.match = hedger.Match(
            round_=0,
            index=0,
            top=self.entry_a,
            bottom=self.entry_b,
            result=Result.TOP_WINS
        )

    def test_match_with_two_entries(self):
        match = hedger.Match(
            round_=0,
            index=0,
            top=self.entry_a,
            bottom=self.entry_b,
            result=Result.TOP_WINS
        )

        expected = (
            "Match(round_=0, index=0, top=Entry('A'), "
            "bottom=Entry('B'), result=Result.TOP_WINS)"
        )

        self.assertEqual(repr(match), expected)
        self.assertEqual(match.get_winner(), self.entry_a)

    def test_match_with_two_submatches(self):
        submatch_0 = hedger.Match(
            round_=0,
            index=0,
            top=self.entry_a,
            bottom=self.entry_b,
            result=Result.TOP_WINS
        )

        submatch_1 = hedger.Match(
            round_=0,
            index=1,
            top=self.entry_c,
            bottom=self.entry_d,
            result=Result.BOTTOM_WINS
        )

        match = hedger.Match(
            round_=1,
            index=0,
            top=submatch_0,
            bottom=submatch_1,
            result=Result.BOTTOM_WINS
        )

        top_str = (
            "Match(round_=0, index=0, top=Entry('A'), "
            "bottom=Entry('B'), result=Result.TOP_WINS)"
        )
        bottom_str = (
            "Match(round_=0, index=1, top=Entry('C'), "
            "bottom=Entry('D'), result=Result.BOTTOM_WINS)"
        )
        expected_fmt = (
            "Match(round_=1, index=0, top={top}, "
            "bottom={bottom}, result=Result.BOTTOM_WINS)"
        )
        expected = expected_fmt.format(top=top_str, bottom=bottom_str)

        self.assertEqual(repr(match), expected)
        self.assertEqual(match.get_winner(), self.entry_d)

    def test_matches_with_same_entries_are_equal(self):
        duplicate_match = hedger.Match(
            round_=0,
            index=0,
            top=self.entry_a,
            bottom=self.entry_b,
            result=Result.TOP_WINS
        )
        self.assertEqual(self.match, duplicate_match)

    def test_matches_with_different_entries_are_not_equal(self):
        match_with_top_and_bottom_switched = hedger.Match(
            round_=0,
            index=0,
            top=self.entry_b,
            bottom=self.entry_a,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(self.match, match_with_top_and_bottom_switched)

    def test_matches_with_different_rounds_are_not_equal(self):
        match_with_different_round = hedger.Match(
            round_=1,
            index=0,
            top=self.entry_a,
            bottom=self.entry_b,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(self.match, match_with_different_round)

    def test_matches_with_different_indexes_are_not_equal(self):
        match_with_different_index = hedger.Match(
            round_=0,
            index=1,
            top=self.entry_a,
            bottom=self.entry_b,
            result=Result.TOP_WINS
        )
        self.assertNotEqual(self.match, match_with_different_index)

    def test_matches_with_different_results_are_not_equal(self):
        match_with_different_result = hedger.Match(
            round_=0,
            index=0,
            top=self.entry_a,
            bottom=self.entry_b,
            result=Result.BOTTOM_WINS
        )
        self.assertNotEqual(self.match, match_with_different_result)

    def test_matches_and_entries_are_not_equal(self):
        empty_entry = hedger.EmptyEntry()
        self.assertNotEqual(empty_entry, self.match)
        self.assertNotEqual(self.match, empty_entry)

    def test_winner_of_match_with_invalid_result_is_none(self):
        match_with_invalid_result = hedger.Match(
            round_=0,
            index=0,
            top=self.entry_a,
            bottom=self.entry_b,
            result="not a valid result"
        )
        self.assertIsNone(match_with_invalid_result.get_winner())

    def test_get_result_probabilities_of_equally_rated_teams(self):
        entry_1 = hedger.Entry('Team 1', 100)
        entry_2 = hedger.Entry('Team 2', 100)

        match = hedger.Match(
            round_=0,
            index=0,
            top=entry_1,
            bottom=entry_2,
            result=Result.TOP_WINS
        )

        expected = {
            Result.TOP_WINS: .5,
            Result.BOTTOM_WINS: .5
        }

        self.assertDictEqual(match.get_result_probabilities(), expected)

    def test_get_result_probabilities_using_example_from_538_csv(self):
        virginia = hedger.Entry('Virginia', 88.07)
        ohio = hedger.Entry('Ohio', 77.51)

        match = hedger.Match(
            round_=0,
            index=4,
            top=virginia,
            bottom=ohio,
            result=Result.BOTTOM_WINS
        )

        expected = {
            Result.TOP_WINS: .864,
            Result.BOTTOM_WINS: .136
        }

        for result, p in match.get_result_probabilities().items():
            self.assertAlmostEqual(p, expected.get(result), 3)
