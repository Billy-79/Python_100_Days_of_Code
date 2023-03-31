#!/usr/bin/env python3

# Exercise 4 - Variables

# Write a program that switches the values stored in the variables a and b.
# WARNING: Your program should work for different inputs. e.g. any value of a and b.

a = input("a: ")
b = input("b: ")


c = a
a = b
b = c



print("a: " + a)
print("b: " + b)