import unittest

import hedger
from hedger.result import Result


class TournamentTest(unittest.TestCase):
    def test_make_bracket_with_two_teams(self):
        gryffindor = hedger.Entry('Gryffindor')
        slytherin = hedger.Entry('Slytherin')
        entries = [gryffindor, slytherin]
        quidditch_cup = hedger.Tournament(entries)
        bracket = quidditch_cup.make_bracket([Result.TOP_WINS])

        final = hedger.Match(
            round_=0,
            index=0,
            top=gryffindor,
            bottom=slytherin,
            result=Result.TOP_WINS
        )
        expected = [final]
        self.assertEqual(bracket.matches, expected)

    def test_make_all_matches_with_four_teams(self):
        gryffindor = hedger.Entry('Gryffindor')
        ravenclaw = hedger.Entry('Ravenclaw')
        hufflepuff = hedger.Entry('Hufflepuff')
        slytherin = hedger.Entry('Slytherin')
        entries = [gryffindor, ravenclaw, hufflepuff, slytherin]
        quidditch_cup = hedger.Tournament(entries)
        bracket = quidditch_cup.make_bracket(
            [Result.TOP_WINS, Result.BOTTOM_WINS, Result.TOP_WINS]
        )

        semifinal_0 = hedger.Match(
            round_=0,
            index=0,
            top=gryffindor,
            bottom=ravenclaw,
            result=Result.TOP_WINS
        )
        semifinal_1 = hedger.Match(
            round_=0,
            index=1,
            top=hufflepuff,
            bottom=slytherin,
            result=Result.BOTTOM_WINS
        )
        final = hedger.Match(
            round_=1,
            index=0,
            top=semifinal_0,
            bottom=semifinal_1,
            result=Result.TOP_WINS
        )
        expected = [semifinal_0, semifinal_1, final]
        self.assertEqual(bracket.matches, expected)
