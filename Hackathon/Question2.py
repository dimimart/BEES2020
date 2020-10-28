"""
Write a function that takes a list of integer values (say nums). For each nums[i] find out how
many numbers in the list are smaller than it. That is, for each nums[i] you have to count the
number of valid j's such that j != i and nums[j] < nums[i]. The function returns the answer as
a list.
"""

def numFunction(numList):
  counter = 0 #initialize counter
  newList = [] #initialize list
  for index in numList:
    for j in numList:
      if index > j:
        counter += 1
      #end if statement
    #end second for loop
    newList.append(counter)
    counter = 0 #make counter go back to 0 so it can count for other index values
  #end first foor loop
  return newList

nummyList = [8, 1, 2, 2, 3]
print("Given List:", nummyList, "\nOutput List:", numFunction(nummyList))

newNummyList = [6, 5, 4, 8]
print("\nGiven List:", newNummyList, "\nOutput List:", numFunction(newNummyList))
