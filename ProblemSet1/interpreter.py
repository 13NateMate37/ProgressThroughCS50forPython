"""
implement a program that prompts the user for an arithmetic expression and then 
calculates and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, with one space between x and y
and one space between y and z, wherein:

    x is an integer
    y is +, -, *, or /
    z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0.
Assume that, if y is /, then z will not be 0.
"""

def mathsInterpreter():
    # Store user input into multiple variables
    # by splitting the string
    x, y, z = (input("What is your expression?\n")).split()

    # If else flow control
    if y == "+" :
        add = int(x) + int(z)
        return add
    elif y == "-":
         sub = int(x) - int(z)
         return sub
    elif y == "*":
        mul = int(x) * int(z)
        return mul
    elif y == "/":
        div = int(x) / int(z)
        return div
    else:
        return "Invalid Input"

    
print(mathsInterpreter())