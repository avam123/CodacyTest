# example.py
def add_numbers(a, b):
    result = a + b
    return result

def multiply_numbers(a, b):
    result = a * b
    return result

def main():
    # Example of duplicate code
    x = 5
    y = 10
    sum_result = add_numbers(x, y)
    multiply_result = multiply_numbers(x, y)
    
    # Example of code style issue (missing whitespace around operators)
    if x>y:
        print("x is greater than y")
    else:
        print("x is less than or equal to y")

    print("Sum:", sum_result)
    print("Product:", multiply_result)

if __name__ == "__main__":
    main()
