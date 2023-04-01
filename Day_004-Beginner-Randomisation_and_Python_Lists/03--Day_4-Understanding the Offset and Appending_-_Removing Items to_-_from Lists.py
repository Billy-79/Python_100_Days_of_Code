#!/usr/bin/env python3

# Understanding the Offset and Appending/Removing Items to/from Lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
"New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
"Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", 
"Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", 
"Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Print the whole list
print(states_of_america)

# print specific item from a list
print(states_of_america[5])
print(states_of_america[-4])

# Change a value in a list
states_of_america[1] = "Pencilvania"
print(states_of_america)
states_of_america[1] = "Pennsylvania"
print(states_of_america)

# Append a new item at the end of the list
states_of_america.append("NewLand")
print(states_of_america)

# To add more than one new items in a list
states_of_america.extend(["NewLand1", "NewLand2"])
print(states_of_america)

# To remove an item from a list
states_of_america.pop(52)
print(states_of_america)
states_of_america.pop(-1)
print(states_of_america)

# Adding and removing specific value item from a list
states_of_america.append("NewLand1")
print(states_of_america)
states_of_america.remove("NewLand1")
print(states_of_america)

# Remove last item from the list
states_of_america.pop()
print(states_of_america)

# To determine how many items a list has - The length function
print(len(states_of_america))
