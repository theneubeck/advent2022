import os

from a04.main import find_inclusion, find_overlaps


def read_file(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "..", f"{filename}")
    return open(path).read()


def run():
    data = read_file("lines.txt")
    print("first", find_inclusion(data))
    print()
    print("second", find_overlaps(data))
    print()
