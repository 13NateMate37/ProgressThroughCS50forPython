def indoorVoice():
    """
    Will take user input text and make it all lower case.
    """
    # Store the users input
    user_input = str(input("What are we whispering\n"))

    # Lowercasing the input
    hushed_input = user_input.lower()

    # Returning the hushed_input
    return hushed_input

print(indoorVoice())
