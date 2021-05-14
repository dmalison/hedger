def is_str_int(x: str):
    try:
        int(x)
        return True
    except ValueError:
        return False


def is_str_float(x: str):
    try:
        float(x)
        return True
    except ValueError:
        return False
