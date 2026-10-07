def slo_playback():
    """
    This function will replace white space with ..., for the
    imitation of slow playback. 
    """
    # Storing user input into a variable
    user_input = str(input("What do you want me to slow?\n"))

    # Replacing the user input whitepsace with ... 
    slowed_input = user_input.replace(" ", "...")

    # Return the slowed_input to the function call
    return slowed_input

print(slo_playback())