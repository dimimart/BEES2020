# 1. Print “Hello, World!” and “Your NAME” using Python.
print("Hello, World! I'm Diana")

# 2. Create a python code with a comment.
#Here is my comment
int = 5
print(int)

# 3. Create a python code with multiline comments.
x = 5
y = 6
"""this 
is 
a
comment"""
print(y)

# 4. Add two numbers and print the result.
print(5+5)

# 5. Multiply two numbers and print the result.
print(6*6)

# 6. Calculate and print the result of the following numerical expression using Python, 10 + 2 * 3 - 5 / 2
print(float(10 + 2 * 3 - 5 / 2))

# 7. Calculate and print the result of the following numerical expression using Python,
((12 - 4) * (3 - 1)) / 2

"""
8. Run the following code to understand how python input works.

your_name = input("What is your name: ")

print("Welcome to the BEES program,", your_name, "!")

"""
your_name = input("What is your name? ")
print("Welcome to the BEES program, " + your_name)

# 9. Enter a numbers as input from the keyboard and print the number following the text "Your input is".
yourInput = input("Enter number: ")
print("Your input is: " + yourInput)

# 10. Enter two numbers as input from the keyboard and print the sum.
x = float(input("Enter a number for the value of x "))
y = float(input("Enter a number for the value of y "))

print(x + y)

"""
11. 
Print the following pattern.
*
**
***
****
*****
"""
string = ["*", "**", "***", "****", "*****"]
for x in string:
  print(x + "\n")
  
"""
12. Calculate and print the result of the following numerical expression after printing the sentence 
"Result of ((2 + 14) / (32 - 20)) * 5 = " in the same line.
((2 + 14) / (32 - 20)) * 5
"""
print('Result of ((2 + 14) / (32 - 20)) * 5 = ' , ((2 + 14) / (32 - 20)) * 5 )

"""
13. Print the follwing two expressions using Python and think about the result.
10 > 5
10 < 5
"""
"""
print(10>5, 10<5)

# 14. Print the expressions 7 + 15 > 16 using Python and think about the result.
print(7 + 15 > 16)
