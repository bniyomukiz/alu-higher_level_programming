#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  for row in matrix:
    for item in row:
      print(str(item).rjust(4), end=" ")
    print()
