class Entry:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        _name_str = "'{name}'".format(name=self._name)
        return "Entry({name_str})".format(name_str=_name_str)

    def __eq__(self, other):
        if isinstance(other, Entry):
            return self._name == other._name
        else:
            return False

    def _get_winner(self):
        return self


class EmptyEntry(Entry):
    def __init__(self):
        super().__init__(None)

    def __repr__(self):
        return "EmptyEntry()"
