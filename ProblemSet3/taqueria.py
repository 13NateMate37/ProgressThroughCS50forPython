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
    total: float = 0.00
    # Customer info print statements
    print("Welcome to Felipe’s Taqueria!")
    print("Here's our menu,")
    # print formatting for appearance
    for item, price in menu.items():
        print(f"{item}: {price}")

    # Starting the loop
    while True:
        # Decision fork in try/except block
        try:
            # Storing user input
            order_item = input("What would you like to order?\n")
            # Storing the funciton call's return value
            price = orderCheck(order_item)
            # Condistional logic to add reutnr value to total variable
            if price is not None:
                total += price
                print(f"Order Total: ${total:.2f}\n")
        # End Of File Error clause to exit loop 
        except EOFError:
            print(f"Your order total is:\n ${total:.2f}")
            break


def orderCheck(ordered_item: str):
    # Titlecasing the variable for dictionary check
    ordered_item = ordered_item.title()
    # Checking the dicitonary for a matching entry and 
    # returning it's price
    if ordered_item in menu:
        return menu[ordered_item]

main()
