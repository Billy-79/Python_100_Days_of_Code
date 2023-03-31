#!/usr/bin/env python3

# Exercise 3 - Adding Even Numbers

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100.
# IMPORTANT: there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation.

# Write your code below this row

even_sum = 0
for number in range(2, 101, 2):
    # print(number)
    even_sum += number
print(even_sum)
  
#or

# alternative_sum = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         # print(number)
#         alternative_sum += number
# print(alternative_sum)