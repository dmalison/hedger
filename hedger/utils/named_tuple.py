import collections


def named_tuple(type_name, field_names):
    return collections.namedtuple(type_name, field_names)
