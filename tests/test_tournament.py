import unittest

import hedger
from hedger.result import Result


class TournamentTest(unittest.TestCase):
    def test_make_bracket_with_four_teams(self):
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
        results = [
            Result.TOP_WINS,
            Result.BOTTOM_WINS,
            Result.TOP_WINS
        ]
        semifinal_0 = hedger.Match(
            round_=0,
            index=0,
            top=gryffindor,
            bottom=ravenclaw,
            result=results[0]
        )
        semifinal_1 = hedger.Match(
            round_=0,
            index=1,
            top=hufflepuff,
            bottom=slytherin,
            result=results[1]
        )
        final = hedger.Match(
            round_=1,
            index=0,
            top=semifinal_0,
            bottom=semifinal_1,
            result=results[2]
        )
        matches = [semifinal_0, semifinal_1, final]

        quidditch_cup = hedger.Tournament(entries)
        bracket = quidditch_cup.make_bracket(results)

        self.assertEqual(bracket.matches, matches)
