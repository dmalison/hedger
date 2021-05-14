import abc

import hedger


class CsvGenerator(abc.ABC):
    def __init__(self, teams):
        self._teams = teams

    @abc.abstractmethod
    def write(self, filepath):
        pass

    def _get_all_brackets(self):
        tournament = self._get_tournament()
        return tournament.make_all_brackets()

    def _get_tournament(self):
        entries = self._get_entries()
        return hedger.Tournament(entries)

    def _get_entries(self):
        return [hedger.Entry(**team) for team in self._teams]
