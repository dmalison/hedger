class Bracket:
    def __init__(self, tournament, results):
        self._tournament = tournament
        self._results = results
        self._winners = None

    @property
    def matches(self):
        return self._tournament.matches

    @property
    def winners(self):
        if self._winners is None:
            self._winners = self._get_winners()
        return self._winners

    def _get_winners(self):
        for match, result in zip(self.matches, self._results):
            match.set_result(result)

        return [match.winner for match in self.matches]
