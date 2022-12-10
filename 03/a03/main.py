import math
import string


def score_lines(input):
    if not input: return dict(sum=0, rows=[])
    lines = input.strip().split("\n")
    rows = []
    for line in lines:
        duplicate = find_duplicate(line)
        rows.append((to_number(duplicate), duplicate))

    return dict(sum=sum(map(lambda x: x[0], rows)), rows=rows)


def to_number(char):
    if char in string.ascii_lowercase:
        return ord(char) - 96
    elif char in string.ascii_uppercase:
        return ord(char) - 38
    raise ValueError(f"unexected char {char}")


def find_duplicate(line):
    half = math.ceil(len(line) / 2)
    one, two = line[half:], line[:half]
    memory = {c: 1 for c in one}

    for c in two:
        if c in memory:
            return c

    raise ValueError("No duplicates")