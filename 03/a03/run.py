from a03.main import score_lines

import os

def read_file(filename):
  path = os.path.join(os.path.dirname(__file__), "..", f"{filename}")
  return open(path).read()

def run():
  data = read_file("lines.txt")
  print("first", score_lines(data))

