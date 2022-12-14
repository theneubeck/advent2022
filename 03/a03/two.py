import string

def group_by_three(lines):
    group_size = 3
    return list(zip(*(iter(lines),) * group_size))


def find_common(lines):
    one, two, three = map(set, lines)
    return (one & two & three).pop()


def scores_badges_in_lines(input):
    if not input: return dict(sum=0, rows=[])
    lines = input.strip().split("\n")

    rows = []
    for group in group_by_three(lines):
        common = find_common(group)
        rows.append((to_number(common), common))

    return dict(sum=sum(map(lambda x: x[0], rows)), rows=rows)


def to_number(char):
    if char in string.ascii_lowercase:
        return ord(char) - 96
    elif char in string.ascii_uppercase:
        return ord(char) - 38
    raise ValueError(f"unexected char {char}")