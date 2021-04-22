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
            self._make_all_matches()
        return self._matches

    def _make_all_matches(self):
        self._matches = list()

        round_ = 0
        last_round_matches = self._entries
        while len(last_round_matches) > 1:
            next_round_matches = self._make_next_round_matches(
                round_,
                last_round_matches
            )
            
            self._matches.extend(next_round_matches)
            round_ += 1
            last_round_matches = next_round_matches

    def _make_next_round_matches(self, round_, last_round_matches):
        index = 0
        next_round_matches = list()
        for top, bottom in utils.grouper(
            last_round_matches,
            n=2,
            fillvalue=entry.EmptyEntry()
        ):
            new_match = match.Match(
                round_=round_,
                index=index,
                top=top,
                bottom=bottom
            )
            next_round_matches.append(new_match)
            index += 1

        return next_round_matches