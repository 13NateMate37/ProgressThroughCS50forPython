def camelTo_snake():
    # Storing user input
    user_input = input("Please type in camelCase. ")

    # blank output variable 
    snake_case = ""

    # Initialising for loop 
    for character in user_input:
        # Condition to catch uppercase and convert it 
        if character.isupper():
            snake_case += "_" + character.lower()
        # Condition for everything else
        else:
            snake_case += character
    # Return the value 
    return snake_case

print(camelTo_snake())