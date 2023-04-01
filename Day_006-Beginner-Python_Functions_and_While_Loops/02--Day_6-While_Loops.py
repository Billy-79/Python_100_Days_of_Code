#!/usr/bin/env python3

# While Loops

# A while loop do something repeatedly while a particular condition is True.
i = 0

while i <= 10:
    print(i)
    i += 1
    

# A while loop will continue running until the specified condition becomes False
# Therefore, there are occasions where a condition of a while loop may never becomes False.
# Such loops known as infinite loops.

# Example of an infinite while loop.
import time
i = 0
while 5 > 3:
    print(i)
    i += 1
    time.sleep(1)
