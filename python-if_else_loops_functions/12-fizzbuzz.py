#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
            if number % 3 == 0:
                print("Fizz ", end="")
                if number % 5 == 0:
                    print("Buzz ", end="")
                else:
                    print("{} ".format(number), end="")