#!/usr/bin/env python3

# Defining and Calling Python Functions

# A function has a name followed by a set of parentheses.

# A function that we're using a lot - The Print Function: Print what is between the paranthese in the console.
print("Hello World!")

# All the functions work pretty much the same.

# Then Len Function: Display for example how many characters are there in a string between the parenthses.
num_char = len("Hello World!")
print(num_char)

# Functionality has been achieved by these built-in functions in Python, like print and len.

# Now what if we wanted to make our own functions, in order to serve our own specific purpose?

# To make our own function we first start with a keyword, which called "def".
# And this is because we're creating or defining our function.
# After the "def" keyword, we can give our function a name (e.g. "my_function").
# Now, the thing that differentiates a function from a variable, however is the parentheses.
# So after the name comes the parentheses, and now the final thing to our function definition is a colon.
# The colon says that everything that comes after that line and is indented belongs with the function

def my_function():
    print("Hello")
    print("Bye")

# Now we've made a very simple function, it's ready, but that's just the definition.
# If we run the code now neither of the print statements that belongs to the function will be executed.
# In order to make it work, we must call the function.

# To call a function we must enter the name of the function followed by a set of parentheses and
# any necessary inputs. In our case, our function doesn't require any inputs, so we can leave 
# the parentheses blank.

my_function()

# We mostly use custom functions when we have to repeat the same code again and again.
# So instead of repeating (e.g. 10 lines of code) we call a function that has this custom functionality.
# Finally indentation is very important, because defines what code belongs where.
# By the Python Style Guide PEP 8 is recommended 4 spaces for every indentation.

# Encapsulation is one of the key concepts of object-oriented languages like Python. Encapsulation is used to restrict access to methods
# and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.
# Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit.
# In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of 
# their current class.