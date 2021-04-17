from Typing import List

from round import Round
from team import Team


class Tournament:
    def __init__(self, teams: List[Team]):
        self._teams = teams
        self._rounds = self._make_rounds()

    def _make_rounds(self):
        self._make_first_round()
        print('making rounds')

    def _make_first_round(self):
        Round()
