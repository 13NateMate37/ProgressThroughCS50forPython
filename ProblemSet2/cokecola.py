# Fucntionally a vending machine
# only takes 25, 10 and 5 cents inputs
# coke cost 50 cents
# after acheving 50 threshold output 
# the users change


def coke_vending_machine():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in (25, 10, 5):
            amount_due -= coin

    print(f"Change Owed: {-amount_due}")

coke_vending_machine()


