import hedger
from hedger import utils


class Tournament:
    def __init__(self, entries):
        self._entries = entries

    def make_bracket(self, results):
        matches = list()
        result_iter = iter(results)

        round_ = 0
        last_round_matches = self._entries
        while len(last_round_matches) > 1:
            this_round_matches = self._make_this_round_matches(
                round_,
                last_round_matches,
                result_iter
            )

            matches.extend(this_round_matches)
            round_ += 1
            last_round_matches = this_round_matches

        return hedger.Bracket(matches)

    def _make_this_round_matches(
        self,
        round_,
        last_round_matches,
        result_iter
    ):
        index = 0
        next_round_matches = list()
        for top, bottom in utils.pairwise_grouper(
            last_round_matches,
            fillvalue=hedger.EmptyEntry()
        ):
            new_match = hedger.Match(
                round_=round_,
                index=index,
                top=top,
                bottom=bottom,
                result=next(result_iter)
            )
            next_round_matches.append(new_match)
            index += 1

        return next_round_matches
