"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be,
an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

# Template code is provided
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# I fill in
def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0:2].isalpha():
        return False
    elif not s.isalnum():
        return False

     # I had to look up the logic for this 
     # So, initalise a variable that is a tracker for
     # whether a number has been seen.
    seen_digit = False

    # Loop over each character in the variable s,
    # which is being fed the value of plate.
    for character in s:
        # This part of the loop checks if the value is 
        # a digit ("number"), * / ^ 
        if character.isdigit():
            # * if the value is a digit, the variable,
            # seen_digit, has a value of false, and the 
            # value that triggers this is exactly 0, 
            # move to return False.
            #  
            # The first value that makes it here that's 
            # not 0 will move to make seen_digit 
            # become True        
            if not seen_digit and character == "0":
                return False
            seen_digit = True
        
         # ^ if not, we move to here where this
         # logic checks if the value of seen_digit 
         # is True. Because it's not True, return 
         # isn't fired and we loop to the next character 
        elif seen_digit:
            # If a non digit makes it here, 
            # after seen_digit has been set 
            # to True, the function will return false.
            return False
    
    # The call ends here, after having gone through 
    # all 6 characters without hitting a return in the loop
    return True

    
main()