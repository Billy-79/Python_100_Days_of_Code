#!/usr/bin/env python3

# Nested if statements and else statements
# Exercise 3 - Leap Year

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an 
# extra day in February.
# This is how you work out whether if a particular year is a leap year.
# 1. Check if the year (e.g. 2000) is evenly divisible by 4. [ 2000 / 4 = 500 ]
# 2. If evenly divisible by 4 then check if the year (e.g. 2000) is also evenly divisible by 100. [ 2000 / 100 = 20 ]
# 3. If evenly divisible by 100 then the year (e.g. 2000) should also evenly divisible by 400 to be a leap year. [ 2000 / 400 = 5 ]
# So if a year is evenly divisible by 4, but not evenly divisible by 100 is a leap year. On the other hand if it's also evenly  
# divisible by 100, it should be evenly divisible by 400 as well to be a leap year. Otherwise it's not a leap year.

# Don't change the code below
year = int(input("Which year do you want to check? "))
# Don't change the code above

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")