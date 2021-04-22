import unittest

import marchmadness.entry as entry
import marchmadness.match as match


class MatchTest(unittest.TestCase):
    def test_match_repr_with_only_round_and_index(self):
        final = match.Match(round_=0, index=0)
        self.assertEqual(repr(final), "Match(round_=0, index=0)")

    def test_match_repr_with_top_entry(self):
        bulldogs = entry.Entry('Bulldogs')
        final = match.Match(round_=0, index=0, top=bulldogs)

        expected = "Match(round_=0, index=0, top=Entry('Bulldogs'))"
        self.assertEqual(repr(final), expected)

    def test_match_repr_with_bottom_entry(self):
        tigers = entry.Entry('Tigers')
        final = match.Match(round_=0, index=0, bottom=tigers)

        expected = "Match(round_=0, index=0, bottom=Entry('Tigers'))"
        self.assertEqual(repr(final), expected)

    def test_match_repr_with_top_and_bottom_entries(self):
        bulldogs = entry.Entry('Bulldogs')
        tigers = entry.Entry('Tigers')
        final = match.Match(round_=0, index=0, top=bulldogs, bottom=tigers)

        top_str = "Entry('Bulldogs')"
        bottom_str = "Entry('Tigers')"
        expected_fmt = "Match(round_=0, index=0, top={top}, bottom={bottom})"
        expected = expected_fmt.format(top=top_str, bottom=bottom_str)

        self.assertEqual(repr(final), expected)

    def test_match_repr_with_semifinals(self):
        bulldogs = entry.Entry('Bulldogs')
        gators = entry.Entry('Gators')
        semifinal_east = match.Match(
            round_=0,
            index=0,
            top=bulldogs,
            bottom=gators
        )

        tigers = entry.Entry('Tigers')
        crimson_tide = entry.Entry('Crimson Tide')
        semifinal_west = match.Match(
            round_=0,
            index=1,
            top=tigers,
            bottom=crimson_tide
        )

        final = match.Match(
            round_=1,
            index=0,
            top=semifinal_east,
            bottom=semifinal_west
        )

        top_str = (
            "Match(round_=0, index=0, "
            "top=Entry('Bulldogs'), "
            "bottom=Entry('Gators'))"
        )
        bottom_str = (
            "Match(round_=0, index=1, "
            "top=Entry('Tigers'), "
            "bottom=Entry('Crimson Tide'))"
        )

        expected_fmt = "Match(round_=1, index=0, top={top}, bottom={bottom})"
        expected = expected_fmt.format(top=top_str, bottom=bottom_str)
        self.assertEqual(repr(final), expected)
