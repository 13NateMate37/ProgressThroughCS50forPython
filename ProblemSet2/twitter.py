# take user text input and drop all vowels in the output

def main():
    print(twitterer())

def twitterer():
    # Storing user input
    user_input = str(input("Your text here: \n"))

    # Setting up my list of vowels for iteration against
    vowel_list = ["a", "e", "i", "o", "u"]

    # An empty variable to store iterated values
    # and print to terminal
    twttrd = ""

    # From left to righ go over each character
    for character in user_input:
        # is the lowercase version of that character 
        # is not in vowel_list, add that character
        # to twttrd
        if character.lower() not in vowel_list:
            twttrd += character
        # if it is a vowel, pass over it.
        else:
            pass

    return twttrd

main()