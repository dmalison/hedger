import itertools


class Tournament:
    def __init__(self, entries):
        self._entries = entries
        self._matches = None

    @property
    def matches(self):
        if self._matches is None:
            self._make_matches()
        return self._matches
    
    def _make_matches(self):
        pass