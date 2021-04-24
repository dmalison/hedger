import marchmadness
from marchmadness import utils


class Tournament:
    def __init__(self, entries):
        self._entries = entries

    def make_bracket(self, results):
        matches = list()
        result_iter = iter(results)

        round_ = 0
        last_round_matches = self._entries
        while len(last_round_matches) > 1:
            round_matches = self._make_round_matches(
                round_,
                last_round_matches,
                result_iter
            )

            matches.extend(round_matches)
            round_ += 1
            last_round_matches = round_matches

        return marchmadness.Bracket(matches)

    def _make_round_matches(self, round_, last_round_matches, result_iter):
        index = 0
        next_round_matches = list()
        for top, bottom in utils.grouper(
            last_round_matches,
            n=2,
            fillvalue=marchmadness.EmptyEntry()
        ):
            new_match = marchmadness.Match(
                round_=round_,
                index=index,
                top=top,
                bottom=bottom,
                result=next(result_iter)
            )
            next_round_matches.append(new_match)
            index += 1

        return next_round_matches
