#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number % 10)
print("last digit of", number, "is", Last_digit, end=" ")
if Last_digit > 5:
    print("and is greater than 5")
if Last_digit == 0:
    print("and is zero")
if Last_digit < 6 and Last_digit != 0:
    print("and is less than 6 and not 0")
