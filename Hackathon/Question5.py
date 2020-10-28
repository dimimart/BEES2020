"""
Based on our definition, a magic number is a number that has at least 3 distinct prime factors.
Write a program that takes in a positive integer number (N) and prints out the first N magic
numbers.
"""

#Shorter version of the code above
def checkPrime(inputNum):
  if inputNum == 1 or inputNum == 2: return True
  for index in range(2, (inputNum//2)+1):
    if (inputNum % index) == 0: return False
  return True

def magicNums(nummy):
  primeList = [] #initialize primeList
  for index in range(2, nummy + 1): #go back to prior assignments when I did this
    if (nummy % index) == 0:
      if (checkPrime(index)): primeList.append(index)
  return primeList

j = 2
if j == 2: #only works with an if statement??
  num = int(input("Enter a number: "))
  value, count = 1, 0
  while True:
    if (checkPrime(value) == False):
      primeVal = magicNums(value) #THIS IS AN INT NOT A LIST
      if len(primeVal) >= 3:
        print(value)
        count += 1
      if (count == num): break
    value += 1
