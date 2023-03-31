#!/usr/bin/env python3

# Python Variables
name = "George"
print(name)

name = "Mary"
print(name)


name = input("What is your name? ")
length = len(name)
print(length)


# Notes:

# Allowed Variable Names in Python:
# 1. We can start variable names with either lowercase or uppercase letters.
# 2. We can start variable names with an underscore sign ( _ ).
# 3. We can use underscore ( _ )to separate two words in a variable name.
# 4. We can use numbers in a variable name as long as the number is not the first character of the variable name.

# Illegal Variable Names in Python:
# 1. We cannot start a variable name with a dash (-).
# 2. We cannot use a dash (-) to separate words in a variable name.
# 3. Variable names cannot start with a number.
# 4. We cannot use space to separate words in a variable name.
# 5. We cannot use Python reserved keywords as variable names.
# To find a list of keywords we can import the module keyword to extract a list of Python reserved keywords(See below).
""" import keyword
    print(keyword.kwlist)
 
    Output:
    ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
    'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']"""
# 6. We cannot use Python built-in function names as variables.

# Best Practices for Creating Variables:
# 1. Python recommends variable names to be lowercase and separated by underscores if there is more than one word in the name.
# 2. Python recommends using descriptive variable names that describe what the object is about for easy readability.
# 3. When naming a class, Python recommends starting each word with a capital letter.
# 4. Avoid using abbreviations as they are not descriptive enough.
# 5. If you are using one letter variable names, avoid using small letters of letters such as O and L 
#    because they can be confused with numbers 0 and 1.
# 6. It is also important to ensure that we keep the variable names as concise as possible.
# 7. Variable names that are unnecessary too long should be avoided.

# Variables do not need to be declared with any particular type.
# Variable names are case-sensitive.
