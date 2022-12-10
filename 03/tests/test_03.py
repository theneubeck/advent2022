import pytest

from a03.main import find_duplicate, score_lines, to_number


# @pytest.mark.skip()
def test_example_input():
    input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
    result = score_lines(input)
    assert result["sum"] == 157, result
    assert result["rows"] == [(16, "p"), (38, "L"), (42, "P"), (22, "v"), (20, "t"), (19, "s")], result


@pytest.mark.parametrize(
    "number, char",
    [
        (1, "a"),
        (26, "z"),
        (27, "A"),
        (52, "Z"),
        (16, "p"),
        (38, "L"),
        (42, "P"),
        (22, "v"),
        (20, "t"),
        (19, "s"),
    ],
)
def test_map_char_to_number(number, char):
    assert to_number(char) == number


@pytest.mark.parametrize(
    "line, duplicate",
    [
        ("abcb", "b"),
        ("aacbbc", "c"),
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ],
)
def test_find_duplicate(line, duplicate):
    assert find_duplicate(line) == duplicate
