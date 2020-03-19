#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]

  rps = ["rock", "paper", "scissors"]
  indices = [0] * n # every element is index to rps array

  outter_list =  []
  
  outter_count = 0
  increament_index = 0

  # loop 3^n times
  while outter_count < 3 ** n:
    index = 0
    inner_list = []

    while index < n:
      inner_list.append(rps[indices[index]])
      index += 1

    outter_list.append(inner_list)
    outter_count += 1

    if indices[increament_index] < 2:
      indices[increament_index] += 1
    else:
      while increament_index < len(indices) - 1:
        if indices[increament_index + 1] < 2:
          for i in range(increament_index + 1):
            indices[i] = 0

          indices[increament_index + 1] += 1
          increament_index = 0
          break
        else:
          increament_index += 1 
  
  return outter_list


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

print(rock_paper_scissors(4))
