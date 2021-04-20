import unittest

import marchmadness.entry as entry
import marchmadness.match as match


class MatchTest(unittest.TestCase):
    def test_match_repr_with_only_name(self):
        final = match.Match('Final')
        self.assertEqual(repr(final), "Match('Final')")

    def test_match_repr_with_top_entry(self):
        final = match.Match('Final')
        bulldogs = entry.Entry('Bulldogs')
        final.set_top(bulldogs)

        self.assertEqual(repr(final.top), "Entry('Bulldogs')")
        expected = "Match('Final').set_top(Entry('Bulldogs'))"
        self.assertEqual(repr(final), expected)

    def test_match_repr_with_bottom_entry(self):
        final = match.Match('Final')
        tigers = entry.Entry('Tigers')
        final.set_bottom(tigers)

        self.assertEqual(repr(final.bottom), "Entry('Tigers')")
        expected = "Match('Final').set_bottom(Entry('Tigers'))"
        self.assertEqual(repr(final), expected)

    def test_match_repr_with_both_top_and_bottom_entries(self):
        final = match.Match('Final')
        bulldogs = entry.Entry('Bulldogs')
        tigers = entry.Entry('Tigers')
        final.set_top(bulldogs).set_bottom(tigers)

        self.assertEqual(repr(final.top), "Entry('Bulldogs')")
        self.assertEqual(repr(final.bottom), "Entry('Tigers')")

        expected = (
            "Match('Final')"
            ".set_top(Entry('Bulldogs'))"
            ".set_bottom(Entry('Tigers'))"
        )

        self.assertEqual(repr(final), expected)

    def test_match_repr_with_semifinals(self):
        final = match.Match('Final')
        semifinal_east = match.Match('Semifinal (East)')
        semifinal_west = match.Match('Semifinal (West)')

        bulldogs = entry.Entry('Bulldogs')
        gators = entry.Entry('Gators')
        tigers = entry.Entry('Tigers')
        crimson_tide = entry.Entry('Crimson Tide')

        semifinal_east.set_top(bulldogs).set_bottom(gators)
        semifinal_west.set_top(tigers).set_bottom(crimson_tide)
        final.set_top(semifinal_east).set_bottom(semifinal_west)

        top_str = (
            "Match('Semifinal (East)')"
            ".set_top(Entry('Bulldogs'))"
            ".set_bottom(Entry('Gators'))"
        )
        bottom_str = (
            "Match('Semifinal (West)')"
            ".set_top(Entry('Tigers'))"
            ".set_bottom(Entry('Crimson Tide'))"
        )

        self.assertEqual(repr(final.top), top_str)
        self.assertEqual(repr(final.bottom), bottom_str)

        expected_fmt = "Match('Final').set_top({top}).set_bottom({bottom})"
        expected = expected_fmt.format(top=top_str, bottom=bottom_str)
        self.assertEqual(repr(final), expected)
