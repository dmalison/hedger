class Match:
    def __init__(self, top, bottom, winner):
        self._top = top
        self._bottom = bottom
        self._winner = winner

    def __repr__(self):
        return 'Match({top}, {bottom}, {winner})'.format(
            top=repr(self._top), 
            bottom=repr(self._bottom),
            winner=repr(self._winner)
        )
