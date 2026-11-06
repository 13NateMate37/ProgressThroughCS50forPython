"""
 implement a program that prompts the user for items, one per line, 
 until the user inputs control-d (which is a common way of ending one’s 
 input to a program). Then output the user’s grocery list in all uppercase, 
 sorted alphabetically by item, prefixing each line with the number of 
 times the user inputted that item. No need to pluralize the items. 
 
 Treat the user’s input case-insensitively.
"""


def main():
    # Initalise empty dictionary
    grocery_list = {}

    # Establishing a loop 
    while True:
        # Establishing a try/except block
        try:
            # Capturing the user input
            item = input("Grocery List:\n")

            # Controlling the input
            item = item.lower()

            # Add item to the dictionary
            grocery_list[item] = grocery_list.get(item, 0)+1
        except EOFError:
            return Processed_List(grocery_list)


def Processed_List(input_dictionary: dict):
    # Sorting the keys for dictionary for alphabetical display
    sorted_keys = sorted(input_dictionary)

    # Looping through that list against the dictionary
    for key in sorted_keys:
        # Gets the count of the item (key)
        count = input_dictionary[key]
        # uppercases the key
        item = key.upper()
        # Stored into variables for working with

        # Printing the grocery list
        print(f"{count} {item}")

main()
