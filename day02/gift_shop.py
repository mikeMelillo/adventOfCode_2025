from functools import reduce

file = "day02/input.txt"
#file = "day02/sample.txt"

with open(file, "r") as file:
  line = file.readline()

ranges = line.split(",")

# def has_repeating_pattern(input: int, digits: int = 1) -> bool:
#   counter = 1
#   str_input = str(input)
#   test = str_input[0:digits*counter]
#   print(f"Test Val: {test}, Digits:{digits}")
#   if digits > len(test)+1//2:
#     print("Break point")
#     return False
#   sample = test[0:digits*counter+1]
#   print(f"Initial Sample: {sample}")
#   while len(sample) == digits:
#     print(f"Sample: {sample}")
#     if sample == test:
#       print(f"Match, Digits: {digits}, Counter: {counter}, Len Input: {len(str_input)}")
#       if digits * counter == len(str_input):
#         return True
#       counter += 1
#       sample = str_input[digits*counter-1:digits*counter]
#       print(f"New Sample: {sample}")
#     else:
#       print("No Match")
#       break
#   has_repeating_pattern(input, digits+1)

def has_repeat_pattern(input: int):
  string_input = str(input)
  #print(string_input)
  length = len(string_input)
  #print(length)
  if  length % 2 != 0:
    return False
  l2 = length//2
  first_chunk = string_input[:l2]
  second_chunk = string_input[l2:]
  return first_chunk == second_chunk

repeaters = []

for r in ranges:
  nums = r.split("-")
  first = int(nums[0])
  last = int(nums[1]) + 1
  x = range(first,last)
  #print(x)
  for num in x:
    if has_repeat_pattern(num,):
      #print(f"**{num}")
      repeaters.append(num)
    else:
      pass
      #print(f"--{num}")

#print(repeaters)
total = reduce(lambda x,y: x+y, repeaters)
print(f"Total: {total}")