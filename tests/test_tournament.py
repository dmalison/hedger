import unittest

import marchmadness.entry as entry
import marchmadness.tournament as tournament


class TournamentTest(unittest.TestCase):
    def test_make_all_matches_with_two_teams(self):
        gryffindor = entry.Entry('Gryffindor')
        slytherin = entry.Entry('Slytherin')
        entries = [gryffindor, slytherin]
        quidditch_cup = tournament.Tournament(entries)
        actual = [repr(m) for m in quidditch_cup.matches]

        top_str = "Entry('Gryffindor')"
        bottom_str = "Entry('Slytherin')"
        final_fmt = "Match(round_=0, index=0, top={top}, bottom={bottom})"
        final_str = final_fmt.format(top=top_str, bottom=bottom_str)
        expected = [final_str]
        self.assertEqual(actual, expected)

    def test_make_all_matches_with_four_teams(self):
        gryffindor = entry.Entry('Gryffindor')
        ravenclaw = entry.Entry('Ravenclaw')
        hufflepuff = entry.Entry('Hufflepuff')
        slytherin = entry.Entry('Slytherin')

        entries = [gryffindor, ravenclaw, hufflepuff, slytherin]
        quidditch_cup = tournament.Tournament(entries)
        actual = [repr(m) for m in quidditch_cup.matches]

        gryffindor_str = "Entry('Gryffindor')"
        ravenclaw_str = "Entry('Ravenclaw')"
        hufflepuff_str = "Entry('Hufflepuff')"
        slytherin_str = "Entry('Slytherin')"

        match_fmt = \
            "Match(round_={round_}, index={index}, top={top}, bottom={bottom})"
        semifinal_0_str = match_fmt.format(
            round_=0,
            index=0,
            top=gryffindor_str,
            bottom=ravenclaw_str
        )
        semifinal_1_str = match_fmt.format(
            round_=0,
            index=1,
            top=hufflepuff_str,
            bottom=slytherin_str
        )
        final_str = match_fmt.format(
            round_=1,
            index=0,
            top=semifinal_0_str,
            bottom=semifinal_1_str
        )
        expected = [semifinal_0_str, semifinal_1_str, final_str]
        self.assertEqual(actual, expected)
