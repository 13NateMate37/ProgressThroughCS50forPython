# If the user input gretting is hello return 0 dollars
# If if H but not hello give $20
# If any other gretting return $100

def kramer_bit():
    # Store the user input
    user_input = input("Greeting: \n")

    # Controlling the user input for operations 
    user_input = str(user_input.strip()).lower()

    # Logic of operation
    if "hello" in user_input:
        return "$0"
    # Matching the index's value for just a h
    elif user_input[0] == "h":
        return "$20"
    else:
        return "$100"

print(kramer_bit())