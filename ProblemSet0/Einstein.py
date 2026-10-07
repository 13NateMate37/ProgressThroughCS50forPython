# Converts a mass (Kg) to energy (joules)

def massToJoules():
    # Storing user input
    user_input = input("How much mass (in kg)?:\n ")

    # Setting the formula variables (E=mc2)
    m = int(str(user_input).strip("kg").strip("KG").strip("Kg"))
    c = 300000000
    E = m * c ** 2

    return print(f"m: {m}" f"\n E: {E}")

print(massToJoules())