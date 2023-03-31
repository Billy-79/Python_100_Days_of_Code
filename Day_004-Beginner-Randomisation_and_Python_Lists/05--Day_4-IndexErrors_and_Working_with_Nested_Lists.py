#!/usr/bin/env python3

# IndexErrors and Working with Nested Lists

# The most common error in lists is the "IndexError: list index out of range"
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", 
"Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Print the length of the list
print(len(dirty_dozen))

# There are 12 items in this list, but to print the last item
print(dirty_dozen[11])

# That's because the first item has index number "0", so print(dirty_dozen[12]) will produce an IndexError
print(dirty_dozen[0])

# A way to manipulate this error is the following
num_of_items = len(dirty_dozen)

print(dirty_dozen[num_of_items - 1])


# Nested lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", ]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen_2 = [fruits, vegetables]

# If we print this list we'll see that there are two square brackets at the beginning and at the end. The reason for this is because 
# there are two lists nested in there
print(dirty_dozen_2)

# To print a specific item from such a list we must use two index numbers, the first to select the nested list we want and the second
# to select the item. So to print from the first list (the one with the fruits) the "Apples" item
print(dirty_dozen_2[0][2])