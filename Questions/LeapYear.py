# Program to check if given year is a leap year.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print(year, "is a leap year.")
    elif year % 400 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
else:
    print(year, "is not a leap year.")
