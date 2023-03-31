#!/usr/bin/env python3

# Project: Calculator (Flags and Recursion)

import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")
    
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
    
def exponent(n1, n2):
    return n1 ** n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True    # Flag
 
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        cont_new_quit = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or 'q' to quit: ")
        if cont_new_quit == "y":
            num1 = answer
        elif cont_new_quit == "q":
            return print("Goodbye")
        else:
            should_continue = False
            cls()
            calculator()    # Recursion

calculator()