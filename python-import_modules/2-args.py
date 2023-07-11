#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    print("arguments:", num_args, end="")
    if num_args == 0:
        print(".", end="")
    print()

    if num_args > 0:
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(i, ":", arg)
