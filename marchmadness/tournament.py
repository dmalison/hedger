from Typing import List

from team import Team


class Tournament:
    def __init__(self, teams: List[Team]):
        self._teams = teams
        self._matches = self._make_matches()

    def _make_matches(self):
        print('making matches')
