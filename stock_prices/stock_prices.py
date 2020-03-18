#!/usr/bin/python

import argparse

# 1st atempt
# def find_max_profit(prices):
  
#   highest_value = None
#   highest_index = None

#   lowest_value = None

#   is_profit = True

#   # check empty list
#   if len(prices) <= 1:
#     return 0
#   else:
#     highest_value = prices[0]
#     highest_index = 0
#     lowest_value = prices[0]

#   # Find highest value
#   for i in range(len(prices) - 1):
#     if prices[i + 1] > highest_value:
#       highest_value = prices[i + 1]
#       highest_index = i + 1

#   # if the highest value is at index: 0, find next highest value
#   # and set it as lowest value (Find the least loss)
#   if highest_index == 0:
#     is_profit = False
#     lowest_value = prices[1]
#     if len(prices) > 2:
#       for i in range(1, len(prices) - 1):
#         if prices[i + 1] > lowest_value:
#           lowest_value = prices[i + 1]
#   else:
#     # Find lowest value which comes before the highest value
#     for i in range(highest_index - 1):
#       if prices[i + 1] < lowest_value:
#         lowest_value = prices[i + 1]

#   # return profit or loss
#   if is_profit:
#     return highest_value - lowest_value
#   else:
#     return lowest_value - highest_value


def find_max_profit(prices):
  highest_value = None
  highest_index = None
  lowest_value = None
  lowest_index = None

    # Check empty and single list
  if len(prices) <= 1:
    return 0
  else:
    highest_value = prices[0]
    highest_index = 0
    lowest_value = prices[0]
    lowest_index = 0

  # Find highest value and index
  for i in range(len(prices) - 1):
    if prices[i + 1] > highest_value:
      highest_value = prices[i + 1]
      highest_index = i + 1

  # Find the lowest value and index
  for i in range(len(prices) - 1):
    if prices[i + 1] < lowest_value:
      lowest_value = prices[i + 1]
      lowest_index = i + 1
  
  # If the highest index is at the right of lowest index,
  # then highest value - lowest value gives the most profit
  if highest_index > lowest_index:
    return highest_value - lowest_value
  else:
  # If the highest index is at the left of lowest index, 
  # then find next highest value and index
    # Check if there are more prices to the right of lowest index
    if len(prices) - 1 > lowest_index:

      # Find next highest value to the right of the lowest value
      next_highest_value = prices[lowest_index + 1]
      next_lowest_value = None
      for i in range(lowest_index + 1, len(prices)):
        if prices[i] > next_highest_value:
          next_highest_value = prices[i]
      
      # Find the next lowest value to the left of original highest value
      if highest_index != 0:
        next_lowest_value = prices[0]
        for i in range(highest_index):
          if prices[i] < next_lowest_value:
            next_lowest_value = pricespi[i]

      # If the next lowest valuvalue exists,
      # compare (next highest - lowest) and (highest - next lowest),
      # return the greater profit
      if next_lowest_value:
        if next_highest_value - lowest_value > highest_value - next_lowest_value:
          return next_highest_value - lowest_value
        else:
          return highest_value - next_lowest_value
      else:
        # If the highest index is at 0, next_highest_value - lowest_value is the profit
        return next_highest_value - lowest_value

    elif highest_index > 0:
    # If the last element is the smallest value
      lowest_value = prices[0]
      for i in range(highest_index):
        if prices[i] < lowest_value:
          lowest_value = prices[i]
      
      return highest_value - lowest_value
    else:
    # If the highest index is at 0, 
    # then find the next highest value to the right of highest value (loss)
      next_highest_value = prices[1]
      for i in range(1, lowest_index):
        if prices[i] > next_highest_value:
          next_highest_value = prices[i]
      
      return next_highest_value - highest_value


  
  # return loss

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))