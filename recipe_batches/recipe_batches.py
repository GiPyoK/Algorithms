#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  num_of_batches = 0

  # Check empty recipe
  if len(recipe) == 0:
    return 0

  # Initial check
  for key in recipe:
    # Check if recipe items are in ingredients
    if not key in ingredients.keys():
      return 0
    # Check if ingredients have enough quantity
    elif ingredients[key] < recipe[key]:
      return 0

  # If there are enough ingredients, check how many whole batches can be made
  has_enough_ingredients = True
  ing_list = ingredients # make a copy, so the original list won't be mutated
  while has_enough_ingredients:
    for key in recipe:
      if recipe[key] <= ing_list[key]:
        ing_list[key] -= recipe[key]
      else:
        has_enough_ingredients = False
        break
    
    # If all the ingredients have enough quantity, increament number of batches
    if has_enough_ingredients:
      num_of_batches += 1

  return num_of_batches
    


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))