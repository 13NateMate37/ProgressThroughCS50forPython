"""
In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, 
and then outputs, as a percentage rounded to the nearest integer, how much fuel is 
in the tank. If, though, 1% or less remains, output E instead to indicate that the 
tank is essentially empty. And if 99% or more remains, output F instead to indicate
that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt
the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions
like ValueError or ZeroDivisionError.
"""
def main():
    # Establising a loop 
    while True:
        # Setting loop conditions to validate user input
        try:
            # Capturing input as a str and then splitting it 
            x, y = str(input("Please give a proper fraction as X/Y: \n")).split(sep='/')
            # Type casting the variables to int for comparison 
            x = int(x)
            y= int(y)
            # Comparison checks
            if x < 0 or y <= 0 or x > y:
                # Should cause a loop if aby of these conditions are True
                continue
            else:
                # As long as they are all false, main calls fractionToPercent,
                # and breaks the loop after printing
                print(fractionToPercent(x,y))
                break
        # Catch incorrect values for the type cast 
        except ValueError:
            # If met, pass over it abd reprompt
            pass


def fractionToPercent(x:int, y:int):
    # Making a fraction into a percentage
    # Establishing try/except for ZeroDivisionErrors
    try:
        percentage = round(x / y * 100)
    except ZeroDivisionError:
         return "Cannot Divide By Zero"

    # Checking value for output parametrs    
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


main()

    

