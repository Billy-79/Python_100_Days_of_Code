#!/usr/bin/env python3

# Exercise 2 - Debugging Leap Year

# #This produces a type error when you run it.
#That should be hint to check this line below
#to make sure it is an int and not a string.
year = int(input("Which year do you want to check?"))

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