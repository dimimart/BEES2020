"""
1. a) How do you make a variable referring to the integer 2?
b) How do you make a variable referring to a string "hello"?
"""
x = 2
stringGreeting = "hello"

"""
2. Assign strings to the variable x and y that will make the print statement print out “Python is awesome”
  x = ""
  y = ""
  print(x + y)
"""
x = "python"
y = " is awesome"
print(x + y) 
#possible because both are strings, however when its an 
#int and string (diff types) then you need to use a comma

"""
3. Create 3 variables counter, miles, and name as integer, floating point, and string 
and assign values 1000, 1000.5 and "John" respectively. 
Then print the variables and verify the types of the variables using the type() function.
"""
counter = 1000
miles = 1000.5
name = "John"
#operator overloading
print(counter, type(counter), "\n", miles, type(miles), "\n", name, type(name))

# 4. Given x = 1 and y = “ is the loneliest number”, print out the string “1 is the loneliest number”
x = 1
y = "is the loneliest number"
#print(len(y)) <<< use that to find the length of a string
print(x, y)

"""
5. for the variables x = 10, y = 5, z = 15
Print the results of,
* x > y
* x > z
"""
x, y, z, = 10, 5, 15
print(x > y, x > z)

# 6. Convert 5 miles to feet. Take the input from the keyboard and print the output. Hint: 1 miles = 5280 feet.
numOfMiles = float(input("How many miles do you want converted to feet?"))
milesToFeet = 5280
returnNum = numOfMiles * milesToFeet
print("There are", returnNum, "feet in", numOfMiles, "miles.")

# 7. Print out the number of hours in 21600 seconds.
print(((21600/60)/60), "hours")

"""
8. Today’s max temperature in Santa Cruz is 91 degree Fahrenheit. 
Convert this to Celsius by taking input from keyboard. 
**Hint:** Fahrenheit = (Celsius * 9/5) + 32
"""
scF = float(input("What is the temperature in F at Santa Cruz?"))
scC = ((scF-32)*5)/9
print("The temperature in C at Santa Cruz is", scC)

"""
9. Evaluate the following expression by taking input from keyboard,
x + 2xy + y2 + (x/y)
Where, x = 7.5, y = 12
"""
x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))
equ = x + (2*x*y) + (y**2) + (x/y)
print(equ)

"""
10. Consider the following boolean variables,
  a = True
  b = False
  c = True
  
  Print the results of the following boolean statements,
  1. a and b
  2. a or b
  3. a or b and c
  4. a and not (b or c)
  5. a and b and c
"""
a, b, c = True, False, True #initialize booleans
print(a and b)#a and b
print(a or b)#a or b
print(a or b and c)#a or b and c
print(a and not (b or c))#a and not (b or c)
#print(a and not(b or c))
# ~ is "not"
print(a and b and c)#a and b and c
