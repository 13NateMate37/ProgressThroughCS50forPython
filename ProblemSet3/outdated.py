"""
 implement a program that prompts the user for a date, anno Domini, in month-day-year order, 
 formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any
 of the values in the list below:

 Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in 
 either format, prompt the user again. Assume that every month has no more than 31 days; no 
 need to validate whether a month has 28, 29, 30, or 31 days.
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

def main():
    while True:

        try:
            # Capture user input 
            user_input = input("Enter a date (mm/dd/yyyy):\n")
            
            # Logic flow split for just numeric answer
            if "/" in user_input:
                # Splitting the input into multiple vairables 
                month, day, year = user_input.split("/")
                # Making the variables data into Integers
                month = int(month)
                day = int(day)
                year = int(year)
                # Checking month validity
                if month > 12 or month <= 0 or day > 31 or day <= 0 or year <=0:
                    continue
                else:
                    return print(date_Formatter(month, day, year))
                    
                
            # Logic flow split for alphanumeric answer
            elif "/" not in user_input:
                month,day, year = str(user_input).split()
                # Handling the split variables
                month = month.capitalize()
                day = int(split_Stripper(day))
                year = int(year)
                # Checking to see if a month that exists was entered first
                if month not in months or day > 31 or day <= 0 or year <=0:
                    continue
                elif month in months:
                    month = months.index(month) + 1
                    return print(date_Formatter(month, day, year))
                    
            
                else:
                    continue

        except ValueError:
            continue


# 'Helper' functions to keep help simplify things 
def split_Stripper(day: str):
    day = day.strip(",")
    # Will loop through the list and remove delcared values from 
    # the righthand side of the string
    for date_suffix in ("st", "nd", "rd", "th"):
        if day.endswith(date_suffix):
            return day.removesuffix(date_suffix)
    # return for just needing the comma remove                      
    return day

def date_Formatter(month: int, day: int, year: int):
    return f"{year:04d}-{month:02d}-{day:02d}"




main()