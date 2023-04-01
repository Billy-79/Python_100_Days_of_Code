#!/usr/bin/env python3

# Exercise 1 - Odd or Even

# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.

# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

#If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print("This is an even number.")
#Otherwise (number cannot be divided by 2 with 0 remainder).
else:
    print("This is an odd number.")
