# Given code to fill in

def main():
    time = input("What time is it? ")
    hours = convert(time)

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    return int(hour) + int(minute) / 60


if __name__ == "__main__":
    main()