year = int(input("Enter a Year. See if it is a Leap Year! "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The Year {year} is a leap year!")
        else:        
            print(f"The Year {year} is not a leap year.")
    else:
        print(f"The Year {year} is a leap year!")
else:
    print(f"The Year {year} is not a leap year.")



# This code does not work - work on it to get it to work
"""if year % 4 == 0 and year % 100 == 0:
    if year % 400 == 0:
        print(f"The Year {year} is a leap year!")
    else: 
        print(f"The Year {year} is not a leap year.")
else:
    print(f"The Year {year} is not a leap year.") """
