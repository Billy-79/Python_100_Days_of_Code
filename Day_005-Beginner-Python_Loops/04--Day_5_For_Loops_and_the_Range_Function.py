#!/usr/bin/env python3

# For Loops and the Range Function

# for loop with range - this will print the numbers 1 to 9, as the end number "10" not included in the range
for number in range(1, 10):
    print(number)
    
# if we want to include number 10, we should set the range from 1 to 11
for number in range(1, 11):
    print(number)
    
# Note
# Evey time the for loop executed it increase the variable "number" by 1 automatically.
# If we want to increase by any other number (e.g. by 3), we should set this option inside the brackets of the range function.
for number in range(1, 11, 3):
    print(number)