"""
Write a program that reads an integer (greater than 0 and less than 1000) from the console
and flip digits of the number, using the arithmetic operators / and %. The result of the flip
operation should always be a three-digit number. Make sure that your program works for
one, two, and three-digit inputs.
"""

def reverse(num):
  reverse = 0
  while num > 0:
    rev = num % 10
    reverse = (reverse * 10) + rev
    num = num // 10
  return int(str(reverse).ljust(3,'0')) #left aligns a string with character, thats why we need to turn it back to an int

number = int(input("Enter a num between 1 & 999: "))
while number < 0 or number > 999:
  print("invalid, try again")
  number = int(input("Enter a num between 1 & 999: "))
print("Reveresed:", reverse(number))
