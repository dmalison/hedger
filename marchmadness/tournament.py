import marchmadness.entry as entry
import marchmadness.match as match
import marchmadness.utils as utils


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
        self._matches = list()
        for top, bottom in utils.grouper(
            self._entries,
            n=2,
            fillvalue=entry.EmptyEntry()
        ):
            new_match = match.Match('final')
            new_match.set_top(top).set_bottom(bottom)
            self._matches.append(new_match)
