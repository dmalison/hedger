import functools

from hedger import Result


class Match:

    def __init__(self, *, round_, index, top, bottom, result):
        self._round = round_
        self._index = index
        self._top = top
        self._bottom = bottom
        self._result = result

        self._winner = self._get_winner()

    @property
    def round(self):
        return self._round

    @property
    def result(self):
        return self._result

    @property
    def winner(self):
        return self._winner

    def _get_winner(self):
        if self._result == Result.TOP_WINS:
            return self._top.winner
        elif self._result == Result.BOTTOM_WINS:
            return self._bottom.winner

    def get_prob(self):
        results_to_probs = self._get_results_to_probs()
        return results_to_probs.get(self._result)

    def __repr__(self):
        repr_fmt = (
            "Match(round_={round_}, index={index}, top={top}, "
            "bottom={bottom}, result={result})"
        )

        repr_str = repr_fmt.format(
            round_=self._round,
            index=self._index,
            top=self._top,
            bottom=self._bottom,
            result=self._result
        )

        return repr_str

    def __eq__(self, other):
        if isinstance(other, Match):
            is_same = True
            is_same &= (self._round == other._round)
            is_same &= (self._index == other._index)
            is_same &= (self._top == other._top)
            is_same &= (self._bottom == other._bottom)
            is_same &= (self._result == other._result)
            return is_same
        else:
            return False

    def _get_results_to_probs(self):
        rating_diff = self._compute_rating_diff()
        top_win_prob = self._compute_win_probability(rating_diff)
        bottom_win_prob = self._compute_win_probability(-rating_diff)
        return {
            Result.TOP_WINS: top_win_prob,
            Result.BOTTOM_WINS: bottom_win_prob
        }

    def _compute_rating_diff(self):
        top_rating = self._top.winner.rating
        bottom_rating = self._bottom.winner.rating
        return top_rating - bottom_rating

    def _compute_win_probability(self, rating_diff):
        p = 1.0 / (1.0 + 10 ** (-rating_diff * 30.464/400))
        return p
