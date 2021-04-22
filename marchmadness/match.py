class Match:
    def __init__(self, *, round_, index, top=None, bottom=None):
        self._round = round_
        self._index = index
        self._top = top
        self._bottom = bottom

    def __repr__(self):
        repr_fmt = "Match(round_={round_}, index={index}"
        repr_str = repr_fmt.format(round_=self._round, index=self._index)

        if self._top is not None:
            repr_str += ", top={top}".format(top=self._top)

        if self._bottom is not None:
            repr_str += ", bottom={bottom}".format(bottom=self._bottom)

        repr_str += ")"

        return repr_str
