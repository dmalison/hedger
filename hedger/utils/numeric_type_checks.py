def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
