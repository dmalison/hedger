from marchmadness.result import Result


class Match:

    def __init__(self, *, round_, index, top, bottom, result):
        self._round = round_
        self._index = index
        self._top = top
        self._bottom = bottom
        self._result = result

        self._winner = None

    @property
    def winner(self):
        if self._winner is None:
            self._winner = self._get_winner()
        return self._winner

    def _get_winner(self):
        if self._result == Result.TOP_WINS:
            top_is_match_inst = isinstance(self._top, Match)
            return self._top.winner if top_is_match_inst else self._top
        elif self._result == Result.BOTTOM_WINS:
            bot_is_match_inst = isinstance(self._top, Match)
            return self._bottom.winner if bot_is_match_inst else self._bottom
        else:
            return

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
