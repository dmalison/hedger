import unittest

import marchmadness


class TournamentTest(unittest.TestCase):
    def test_make_all_matches_with_two_teams(self):
        gryffindor = marchmadness.Entry('Gryffindor')
        slytherin = marchmadness.Entry('Slytherin')

        entries = [gryffindor, slytherin]
        quidditch_cup = marchmadness.Tournament(entries)

        final = marchmadness.Match(
                round_=0,
                index=0,
                top=gryffindor,
                bottom=slytherin
            )
        expected = [final]

        self.assertEqual(quidditch_cup.matches, expected)

    def test_make_all_matches_with_four_teams(self):
        gryffindor = marchmadness.Entry('Gryffindor')
        ravenclaw = marchmadness.Entry('Ravenclaw')
        hufflepuff = marchmadness.Entry('Hufflepuff')
        slytherin = marchmadness.Entry('Slytherin')

        entries = [gryffindor, ravenclaw, hufflepuff, slytherin]
        quidditch_cup = marchmadness.Tournament(entries)

        semifinal_0 = marchmadness.Match(
            round_=0,
            index=0,
            top=gryffindor,
            bottom=ravenclaw
        )
        semifinal_1 = marchmadness.Match(
            round_=0,
            index=1,
            top=hufflepuff,
            bottom=slytherin
        )
        final = marchmadness.Match(
            round_=1,
            index=0,
            top=semifinal_0,
            bottom=semifinal_1
        )
        expected = [semifinal_0, semifinal_1, final]
        self.assertEqual(quidditch_cup.matches, expected)
