#!/usr/bin/env python3

# Functions with Outputs and Multiple Return Values

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Already used functions with outputs.
length = len(formatted_name)

# Return as an early exit
def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
    
# In the above function the segment inside the triple quotes is called Docstring.
# A Docstring typically comes directly after defining our functions, in order to explain
# shortly what the function does. 