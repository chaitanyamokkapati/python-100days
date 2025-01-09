'''
Write a program that works out whether if a given year is a leap year. A
normal year has 365 days, leap years have 366, with an extra day in
February. 

    on every year that is evenly divisible by 4
        except every year that is evenly divisible by 100
            unless the year is also evenly divisible by 400
            
e.g. The year
2000 + 4 = 500 (Leap)
100=20 (Not Leap)
2000 = 5 (Leap!)
So the year 2()()() is a leap year.

'''

year = int(input("Which year do you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
       if year % 400 == 0:
           print(f"Year {year} is a Leap Year.")
       else:
           print(f"Year {year} is a Not Leap Year.")
    else:
         print(f"Year {year} is a Leap Year.")
else:
    print(f"Year {year} is a Not Leap Year.")