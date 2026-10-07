# prompt the user to input an extention name and 
# return the appropriate suffix 

def extentionMatcher():
    # Storing user input for use
    filename = input("Enter filename + Extension: ").lower()

    # if else Logic chain, to match result.
    if filename.endswith(".gif"):
        return("image/gif")
    elif filename.endswith((".jpg", ".jpeg")):
        return("image/jpeg")
    elif filename.endswith(".png"):
        return("image/png")
    elif filename.endswith(".pdf"):
        return("application/pdf")
    elif filename.endswith(".txt"):
        return("text/plain")
    elif filename.endswith(".zip"):
        return("application/zip")
    else:
        return("application/octet-stream")

print(extentionMatcher())