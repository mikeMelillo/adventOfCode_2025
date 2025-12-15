from enum import Enum

class Direction(Enum):
  LEFT = 0
  RIGHT = 1

file = "day01/input.txt"
#file = "day01/sample_moves.txt"

with open(file, "r") as file:
  lines = file.readlines()

trip_point = 99

clicks = 0

rotations = 0

distance = 0

zero_counts = 0
zero_clicks = 0

position = 50

# def greater_than_check(p):
#   global zero_clicks
#   if p >= 100:
#     p = p - 100
#     zero_clicks += 1
#     return greater_than_check(p)
#   else:
#     return p

# def less_than_check(p):
#   global zero_clicks
#   if p < 0:
#     p = 100 + p
#     zero_clicks += 1
#     return less_than_check(p)
#   else:
#     return p

# for line in lines:
#   print(f"Pos: {position}")
#   last_position = position
#   move = line.strip()
#   print(move)
#   dir = move[0]
#   dist = int(move[1:])
#   if position == 0:
#     zero_counts += 1
#   if dir == "L":
#     position -= dist
#     if last_position > 0 and position <= 0:
#       zero_clicks += 1
#     position = less_than_check(position)
#   if dir == "R":
#     position += dist
#     if last_position < 100 and position >= 100:
#       zero_clicks += 1
#     position = greater_than_check(position)

for line in lines:
  move = line.strip()
  dir = move[0]
  dist = int(move[1:])
  flag = dist > 100
  print(f"xxx: {position}")
  if flag:
    print(f"Starting position: {position}")
    print(f"New line: {move}")
    print(f"Dist: {dist}")
    print(f"Clicks before:{zero_clicks}")
  if position == 0:
    zero_counts += 1
  if dir == "L":
    position -= dist
  elif dir == "R":
    position += dist
  if position > 99:
    zero_clicks += position // 100
    position = position % 100
  elif position < 0:
    zero_clicks += 1 + (abs(position) // 100)
    if flag:
      print(f"Midstep: {position}")
      print(abs(position))
      print(abs(position) % 100)
    position = abs(position) % 100
  if flag:
    print(f"Clicks after: {zero_clicks}")
    print(f"New postion: {position}")


print(f"Part 1 Zeros: {zero_counts}")
print(f"Part 2 Zero Clicks: {zero_clicks}")