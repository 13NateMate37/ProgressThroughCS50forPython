"""
In a file called nutrition.py, implement a program that prompts users 
to input a fruit (case-insensitively) and then outputs the number of 
calories in one portion of that fruit, per the FDA’s poster for fruits, 
which is also available as text. Capitalization aside, assume that users 
will input fruits exactly as written in the poster 
(e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
"""
# Practing defining a main function and routing through that
def main():
    # Storing the user input, making it a lower case string
    user_input = str(input("Item: \n")).lower()

    # Saving the called functions vlaue so it can be printed
    calories = fruits_calories(user_input)
    # As the variable calls to the funciton to recieve 
    # assignment, **

    # *** otherwise the value will be None and the programme 
    # will end, otherwise, the value held by calories is printed
    # to the terminal 
    if calories is not None:
        print(calories)


def fruits_calories(fruit: str):

    # ** it is checked against this list, **
    fruits_list = {
        "apple": 130, 
        "banana": 110, 
        "grapes": 90,
        "melon": 50,
        "orange": 80,
        "pear": 100,
        "plums": 70,
        "strawberries": 50,
        "watermelon": 80
    }
     # ** by this if condition, which will only give a
     # value if the user input is in the dictionary as a key ***
    if fruit in fruits_list:
        return fruits_list[fruit] 

main()