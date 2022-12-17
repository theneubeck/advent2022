import pytest

from a04.main import find_inclusion, find_overlaps, is_contained_in


def test_find_inclusion():
    input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    result = find_inclusion(input)
    assert result.total == 2
    assert result.pairs == [3, 4]


def test_find_overlaps():
    input = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    result = find_overlaps(input)
    assert result.total == 4
    assert result.pairs == [2, 3, 4, 5]


@pytest.mark.parametrize(
    "one,two,overlap",
    [
        (
            "2-4",
            "6-8",
            False,
        ),
        (
            "2-3",
            "4-5",
            False,
        ),
        (
            "5-7",
            "7-9",
            False,
        ),
        (
            "2-8",
            "3-7",
            True,
        ),
        (
            "6-6",
            "4-6",
            True,
        ),
        (
            "2-6",
            "4-8",
            False,
        ),
    ],
)
def test_is_overlapping(one, two, overlap):
    assert is_contained_in(one, two) == overlap
