# example.py

# Unused imports or variables
import os
import sys

def add_numbers(a, b):
    result = a + b
    return result

def multiply_numbers(a, b):
    result = a * b
    return result

def main():
    # Duplicate code
    x = 5
    y = 10
    sum_result = add_numbers(x, y)
    multiply_result = multiply_numbers(x, y)
    
    # Code style issue: missing whitespace around operators
    if x>y:
        print("x is greater than y")
    else:
        print("x is less than or equal to y")

    # Logical complexity: this is a simple check that could be refactored
    if x == 5:
        if y == 10:
            print("x is 5 and y is 10")
        else:
            print("x is 5 but y is not 10")
    else:
        print("x is not 5")

    print("Sum:", sum_result)
    print("Product:", multiply_result)

if __name__ == "__main__":
    main()
