from collections import namedtuple
from typing import Tuple

Result = namedtuple("Result", "total,pairs")


def find_inclusion(input: str) -> Result:
    rows = [line.split(",") for line in input.strip().split("\n") if line]
    if not rows:
        return Result(0, [])
    result = []
    for idx, row in enumerate(rows):
        if is_contained_in(*row):
            result.append(idx)
    return Result(total=len(result), pairs=result)


def find_overlaps(input: str) -> Result:
    rows = [line.split(",") for line in input.strip().split("\n") if line]
    if not rows:
        return Result(0, [])
    result = []
    for idx, row in enumerate(rows):
        if is_overlapping(*row):
            result.append(idx)
    return Result(total=len(result), pairs=result)


Pair = namedtuple("Pair", "start, stop")


def is_overlapping(one: str, two: str):
    set1, set2 = parse(one, two)

    return len(set1.intersection(set2)) > 0


def is_contained_in(one: str, two: str):
    set1, set2 = parse(one, two)

    return len(set1.intersection(set2)) == len(set1) or len(set2.intersection(set1)) == len(set2)


def parse(one: str, two: str) -> Tuple[set]:
    return interval_to_set(one), interval_to_set(two)


def interval_to_set(interval):
    start, stop = interval.split("-")
    return set(range(int(start), int(stop) + 1))
