import unittest
import itertools
import os
import sys
import json
from enum import Enum

def read_file():
  path = os.path.join(os.path.dirname(__file__), "guide.txt")
  return open(path).read()


class Move(Enum):
  Loose = 0
  Draw = 3
  Win = 6

  def parse(string):
    if string == "X":
      return Move.Loose
    elif string == "Y":
      return Move.Draw
    elif string == "Z":
      return Move.Win
    raise ValueError(f'"{string}" not in YXZ')


class Tool(Enum):
  Rock = 1
  Paper = 2
  Scissors = 3

  def parse(string):
    if string in ["A", "X"]:
      return Tool.Rock
    elif string in ["B", "Y"]:
      return Tool.Paper
    elif string in ["C", "Z"]:
      return Tool.Scissors
    raise ValueError(f'"{string}" not in ABC, YXZ')

  def parse_and_score(they, you):
    tool = Tool.parse(they)
    move = Move.parse(you)

    if move == Move.Win:
      if tool == Tool.Rock:
        return score_turn(tool, Tool.Paper)
      elif tool == Tool.Paper:
        return score_turn(tool, Tool.Scissors)
      return score_turn(Tool.Scissors, Tool.Rock)
    elif move == Move.Loose:
      if tool == Tool.Rock:
        return score_turn(tool, Tool.Scissors)
      elif tool == Tool.Paper:
        return score_turn(tool, Tool.Rock)
      elif tool == Tool.Scissors:
        return score_turn(tool, Tool.Paper)

    return score_turn(tool, tool)


def score_turn(they, you):
  score = you.value
  if they == you:
    score = score + 3
  elif you == Tool.Rock and they == Tool.Scissors:
    score = score + 6
  elif you == Tool.Paper and they == Tool.Rock:
    score = score + 6
  elif you == Tool.Scissors and they == Tool.Paper:
    score = score + 6

  return score

def total_score_one(input):
  rows = parse_input(input)
  scores = list(map(lambda x: score_turn(x[0], x[1]), rows))

  return dict(total=sum(scores),rounds=scores)

def total_score(input):
  rows = parse_input_as_turns(input)
  scores = list(rows)

  return dict(total=sum(scores),rounds=scores)



def parse_input(input):
  result = []
  rows = input.strip().split("\n")
  for row in rows:
    result.append(list(map(Tool.parse, row.split())))
  return result

def parse_input_as_turns(input):
  result = []
  rows = input.strip().split("\n")
  for row in rows:
    they, you = row.split()
    result.append(Tool.parse_and_score(they, you))
  return result


class TestAdventOfCode2a(unittest.TestCase):
  def test_score_turns(self):
    assert score_turn(Tool.Rock, Tool.Paper) == 8, score_turn(Tool.Rock, Tool.Paper)
    assert score_turn(Tool.Paper, Tool.Rock) == 1, score_turn(Tool.Paper, Tool.Rock)
    assert score_turn(Tool.Scissors, Tool.Scissors) == 6, score_turn(Tool.Scissors, Tool.Scissors)
    assert score_turn(Tool.Rock, Tool.Rock) == 4, score_turn(Tool.Rock, Tool.Rock)

  def test_parse_input(self):
    result = parse_input("""
A Y
""")
    assert len(result) == 1
    assert result[0] == [Tool.Rock, Tool.Paper], result

  def test_parse_multiline_input(self):
    result = parse_input("""
A Y
B X
C Z
""")
    assert len(result) == 3
    assert result[0] == [Tool.Rock, Tool.Paper], result[0]
    assert result[1] == [Tool.Paper, Tool.Rock], result[1]
    assert result[2] == [Tool.Scissors, Tool.Scissors], result[2]

  def test_total_score_one(self):
    input = """
A Y
B X
C Z
"""
    result = total_score_one(input)
    assert result["total"] == 15, result
    assert result["rounds"] == [8,1,6], result


class TestAdventOfCode2(unittest.TestCase):
  def test_parse_input_as_turns(self):
    [result] = parse_input_as_turns("A Y")
    assert result == 4, result
    [result] = parse_input_as_turns("B Y")
    assert result == 5, result
    [result] = parse_input_as_turns("C Y")
    assert result == 6, result

  def test_parse_and_score(self):
    result = Tool.parse_and_score("A","Y")
    assert result == 4, [result, "A","Y"]
    result = Tool.parse_and_score("B","X")
    assert result == 1, [result, "B", "X"]
    result = Tool.parse_and_score("C","Z")
    assert result == 7, [result, "C", "Z"]


  def test_parse_and_score_all(self):
    result = parse_input_as_turns("""
A X
A Y
A Z
B X
B Y
B Z
C X
C Y
C Z
""")
    assert result[0] == 0 + 3, [result[0], "rock -> scissors (X - loose)"]
    assert result[1] == 3 + 1, [result[1], "rock -> rock (Y - draw)"]
    assert result[2] == 6 + 2, [result[2], "rock -> paper (Z - win)"]

    assert result[3] == 0 + 1, [result[3], "paper -> rock (X - loose)"]
    assert result[4] == 3 + 2, [result[4], "paper -> paper (Y - draw)"]
    assert result[5] == 6 + 3, [result[5], "paper -> scissors (Z - win)"]

    assert result[6] == 0 + 2, [result[6], "scissors -> paper (X - loose)"]
    assert result[7] == 3 + 3, [result[7], "scissors -> scissors (Y - draw)"]
    assert result[8] == 6 + 1, [result[8], "scissors -> rock (Z - win)"]

  def test_total_score_as_turns(self):
    input = """
A Y
B X
C Z
"""
    result = total_score(input)
    assert result["total"] == 12, result
    assert result["rounds"] == [4,1,7], result

  def test_total_score_as_turns_two(self):
    input = """
A X
A Y
A Z
B X
B Y
B Z
C X
C Y
C Z
"""
    result = total_score(input)
    assert result["rounds"] == [3,4,8,1,5,9,2,6,7], result
    assert result["total"] == 45, result



if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "test":
      sys.argv.remove("test")
      unittest.main()
    else:
      print("first", total_score_one(read_file())["total"])
      print("second", total_score(read_file())["total"])
