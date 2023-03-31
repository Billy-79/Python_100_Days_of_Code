#!/usr/bin/env python3

# Functions with Inputs & Positional vs. Keyword Arguments

# Simple Function
def greet():
    print("Hello Bill")
    print("How do you do Mary?")
    print("Isn't the weather nice today?")
greet()

# Function that allows for input
# 'name' is the parameter.
# 'Billy' is the argument.
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Billy")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Calling greet_with() with Positional Arguments
greet_with("George", "Somewhere")
# vs.
greet_with("Somewhere", "George")


# Calling greet_with() with Keyword Arguments
greet_with(location="Athens", name="Jimmy")