import unittest
import itertools
import os
import sys
import json

def find_heaviest_elf(input):
  calorie_list = parse(input)
  elfs = group_by_empty(calorie_list, "")
  elfs_summed = list(map(sum, elfs))
  max_sum = max(elfs_summed)
  position = elfs_summed.index(max_sum)

  return dict(sum=max_sum, position=position)

def find_top_three(input):
  calorie_list = parse(input)
  elfs = group_by_empty(calorie_list, "")
  elfs_summed = list(map(sum, elfs))
  elfs_sorted = sorted(elfs_summed, key=lambda x: -x)

  result = elfs_sorted[:3]

  return dict(
    list = list(map(lambda x: dict(sum=x, position=elfs_summed.index(x)), result)),
    total = sum(result)
  )

def group_by_empty(calorie_list, divider = ""):
  groups = []
  for k, g in itertools.groupby(calorie_list, lambda x: x != divider):
    group = list(g)
    if not (len(group) == 1 and group[0] == ""):
      groups.append(group)
  return groups


def parse(string):
  return map(lambda x: int(x) if(x != "") else x, string.split("\n"))


class TestAdventOfCode1(unittest.TestCase):

  def test_find_heaviest_elf(self):
    input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    result = find_heaviest_elf(input)
    assert result["position"] == 3
    assert result["sum"] == 24000

  def test_find_top_three(self):
    input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
    results = find_top_three(input)
    assert len(results["list"]) == 3
    assert results["total"] == 45000, "result was {}".format(json.dumps(results))
    assert results["list"] == [
      {"sum": 24000, "position": 3},
      {"sum": 11000, "position": 2},
      {"sum": 10000, "position": 4}
    ], "result was {}".format(json.dumps(results))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "test":
      sys.argv.remove("test")
      unittest.main()
    else:
      path = os.path.join(os.path.dirname(__file__), "elfs.txt")
      print("heaviest", find_heaviest_elf(open(path).read()))
      print("top three", find_top_three(open(path).read()))
