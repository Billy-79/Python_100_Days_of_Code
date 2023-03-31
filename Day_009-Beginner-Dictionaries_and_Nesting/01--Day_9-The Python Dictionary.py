#!/usr/bin/env python3

# The Python Dictionary

# Notes: 
# The way we should thing about dictionaries is in form of a table.
# Every dictionary has two parts to it.
# On the left hand side is the key, which is the equivalent of the word in the dictionary, then a colon and finally,
# on the right hand side there is an associated value, which would be the equivalent of the actual definition of the word.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }
    

# To retrieve an item from a dictionary
#print(programming_dictionary["Bug"])

# It's very important to enter the key ("Bug") correctly.
# Also the key should have the same data type. The following won't work
# print(programming_dictionary[Bug])

# How to add a piece of data
programming_dictionary["Loop"] = "The action of dooing something over and over again."
#print(programming_dictionary)

# Also sometimes is very useful to create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# The add method can also be used to edit an item
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

# Loop through a dictionary

# This will print only the keys
for thing in programming_dictionary:
    print(thing)
    
# The following will print both the key and value
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])