class Match:
    def __init__(self, name):
        self._name = name

        self._top = None
        self._bottom = None
        self._winner = None

    @property
    def top(self):
        return self._top

    def set_top(self, top):
        self._top = top
        return self

    @property
    def bottom(self):
        return self._bottom

    def set_bottom(self, bottom):
        self._bottom = bottom
        return self

    def __repr__(self):
        repr_str = "Match('{name}')".format(name=self._name)

        if self._top is not None:
            repr_str += ".set_top({top})".format(top=self._top)

        if self._bottom is not None:
            repr_str += ".set_bottom({bottom})".format(bottom=self._bottom)

        return repr_str
