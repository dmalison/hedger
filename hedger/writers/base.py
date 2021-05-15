import abc

import hedger


class Writer(abc.ABC):
    def __init__(self, teams, path):
        self._teams = teams
        self._path = path

    @abc.abstractmethod
    def write(self):
        pass

    def _get_all_brackets(self):
        tournament = self._get_tournament()
        return tournament.make_all_brackets()

    def _get_tournament(self):
        entries = self._get_entries()
        return hedger.Tournament(entries)

    def _get_entries(self):
        return [hedger.Entry(**team) for team in self._teams]
