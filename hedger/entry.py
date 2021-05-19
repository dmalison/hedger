class Entry:
    def __init__(self, name, rating=None):
        self._name = name
        self._rating = rating

    def __repr__(self):
        name_str = "'{name}'".format(name=self._name)

        if self._rating is None:
            repr_fmt = "Entry({name_str})"
        else:
            repr_fmt = "Entry({name_str}, {rating})"

        repr_str = repr_fmt.format(name_str=name_str, rating=self._rating)

        return repr_str

    def __eq__(self, other):
        if isinstance(other, Entry):
            return self._name == other._name
        else:
            return False

    @property
    def winner(self):
        return self

    @property
    def rating(self):
        return self._rating


class EmptyEntry(Entry):
    def __init__(self):
        super().__init__(None)

    def __repr__(self):
        return "EmptyEntry()"
