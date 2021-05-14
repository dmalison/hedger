import os


def path_exists(path):
    return os.path.exists(path)


def remove(path):
    os.remove(path)
