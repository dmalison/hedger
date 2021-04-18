class Entry:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return "Entry('{name}')".format(name=self._name)
