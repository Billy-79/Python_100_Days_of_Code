#!/usr/bin/env python3

# Random Module

import random

# The commented code is how to create our module
# import my_module
# print(my_module.pi)

# Generate random integer
random_integer = random.randint(1, 10)
print(random_integer)

# Generate random floating point number between 0.0 - 1.0 (not including 1.0)
random_float = random.random()
print(random_float)

# Generate random floating point number between 0.0 - 5.0
random_float = random.random() * 5
print(random_float)

#Back to love calculator
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
