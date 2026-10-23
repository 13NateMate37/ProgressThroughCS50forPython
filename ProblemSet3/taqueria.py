"""
implement a program that enables a user to place an order, prompting them for items, one per line, 
until the user inputs control-d (which is a common way of ending one’s input to a program). After 
each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar 
sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore 
any input that isn’t an item. Assume that every item on the menu will be titlecased.
"""

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    # Initialsing empty variable
    total = 0.00
    print("Welcome to Felipe’s Taqueria!")
    print("Here's our menu,")
    while True:
        try:
            for item, price in menu.items():
                print(f"{item}: {price}")
            print("\n")
            order = input("What would you like to order?\n")

            print(f"Order Total: ${total}")
        except EOFError:
            return total


def order_Item(ordered_item: str):
    # Convert the ordered item string to 
    # a reliable base state
    ordered_item = ordered_item.lower()
    # Titlecasing the variable for dictionary check
    if ordered_item.title() in menu:
        return menu[ordered_item]

main()
