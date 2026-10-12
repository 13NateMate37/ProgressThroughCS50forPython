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

    return amount_due

print(coke_vending_machine())