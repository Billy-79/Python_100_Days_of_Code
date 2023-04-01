#!/usr/bin/env python3

# Exercise 2 - High Score

# You are going to write a program that calculates the highest score from a List of scores.
# IMPORTANT: you are not allowed to use the max or min functions.

# Don't change the code below
student_scores = input("Input a list of student scores separated with a space ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

# Write your code below this row
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

# Print(highest_score)
print(f"The highest score in the class is: {highest_score}")
