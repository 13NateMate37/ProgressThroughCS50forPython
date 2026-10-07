# Code block provided by CS50 for the tip calculator problem. 

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# I am to fill this out
def dollars_to_float(d):
    return float(d.strip("$"))

# I am to fill this out 
def percent_to_float(p):
    p = float(p.strip("%")) / 100
    return p 

main()