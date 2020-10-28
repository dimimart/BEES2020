"""
Write a function that takes an array of integer numbers and an integer target and returns
indices of the two numbers such that they add up to the target.
You may assume that each
input would have exactly one solution, and you may not use the same element twice.
"""

def summy(num_List, target):
  rangeOfNums = {} #initializing set rangeOfNums
  for index in range(len(num_List)):
    num = num_List[index]
    pairOfTwo = target - num
    if (pairOfTwo in rangeOfNums):
      return [rangeOfNums[pairOfTwo], index]
      #end of if statement
    rangeOfNums[num] = index
    #end of for loop
  return None #because nothing is being returned if ^^ is not applicable
  #end of summy function

num_List = [2,7,11,15]
target = 9
print("Nums:", num_List, "\nTarget:", target, "\nSolution:", summy(num_List, target))

nummyList = [58, 2, 8, 4, 0]
target = 1 #unable to get a real solution, therefore this is testing to see if the "return None" works
print("\nNums:", nummyList, "\nTarget:", target, "\nSolution:", summy(nummyList, target))
