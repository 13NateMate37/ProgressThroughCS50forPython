# Raplcing emoticons with emojis
def eConToEji():
    # Store user input 
    user_input = input("Please enter your text here:\n")

    # Converting the emoticons to emojis
    user_input = user_input.replace(
        ":)", "\U0001F642"
        ).replace(
            ":(", "\U0001F641"
            )

    # Returning the output
    return user_input

print(eConToEji())