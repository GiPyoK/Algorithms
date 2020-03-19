#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]

  rps = ["rock", "paper", "scissors"]
  indices = [0] * n # every element is index to rps array
  # [0] == "rock"
  # [1] == "paper"
  # [2] == "scissors"
  # indicies = [0,2,1] == ["rock", "scissors", "paper"]

  outter_list =  []
  
  outter_count = 0 # counter for outter while loop
  indices_index = 0 # loops through indices array

  # loop 3^n times
  while outter_count < 3 ** n:
    inner_count = 0 # counter for inner while loop
    inner_list = []

    # loop n times
    while inner_count < n:
      # append elements in rps array by n times
      # iterate through rps array with index in indices array
      inner_list.append(rps[indices[inner_count]])
      inner_count += 1

    outter_list.append(inner_list)
    outter_count += 1

    # iterate from "rock" to "scissors"
    if indices[indices_index] < 2:
      indices[indices_index] += 1 # move to next element in rps array
    else:
      while indices_index < len(indices) - 1:
        # if the next index is less than 2,
        # then increament the next index and set 0 for all indices before the increamented index
        if indices[indices_index + 1] < 2:
          for i in range(indices_index + 1):
            indices[i] = 0

          indices[indices_index + 1] += 1
          indices_index = 0
          break
        else:
          indices_index += 1 
  
  return outter_list


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

# print(rock_paper_scissors(10))