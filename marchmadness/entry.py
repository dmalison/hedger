class Entry:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        _name_str = "'{name}'".format(name=self._name)
        return "Entry({name_str})".format(name_str=_name_str)


class EmptyEntry(Entry):
    def __init__(self):
        super().__init__(None)

    def __repr__(self):
        return "EmptyEntry()"
