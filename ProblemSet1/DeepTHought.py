# The greatquestion of life,
#  as is in The hitchhikers guide to the glaxy 

def greatQuestion():
     # List of answers for lookup
     correct_answers = ["42", "forty-two", "forty two"]

     # Storing the user input
     user_input = input(
          "What is the answer to the Great Question of Life, the Universe, and Everything?\n"
          ).strip().lower() 

     # Logic to provide a repsone
     if user_input in correct_answers:
          return "Yes"
     else:
          return "No"

print(greatQuestion()) 
      