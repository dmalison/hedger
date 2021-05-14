def is_str_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def is_str_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
