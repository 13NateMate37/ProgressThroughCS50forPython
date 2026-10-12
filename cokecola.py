# Fucntionally a vending machine
# only takes 25, 10 and 5 cents inputs
# coke cost 50 cents
# after acheving 50 threshold output 
# the users change


def coke_vending_machine():
    # Initialise cost variable
    coke_cost = 50

    # Initialise inserted coin variable
    inserted_coin = 0
    
    # Initialise amount due variable
    amount_due = f"Amount due: {(coke_cost - inserted_coin)}"

    # Storing the user input
    user_input = int(input("Insert Coin: "))

    if user_input == 25:
        inserted_coin = inserted_coin + user_input
        print(amount_due)
    elif user_input == 10:
        inserted_coin = inserted_coin + user_input
        print(amount_due)
    elif user_input == 5:
        inserted_coin = inserted_coin + user_input
        print(amount_due)




 

print(coke_vending_machine())