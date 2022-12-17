import os

from a04.main import find_overlap

# from a04.two import scores_badges_in_lines


def read_file(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "..", f"{filename}")
    return open(path).read()


def run():
    data = read_file("lines.txt")
    print("first", find_overlap(data))
    # print("second", scores_badges_in_lines(data)["sum"])
