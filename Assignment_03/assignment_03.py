# Task 1: Calculate Factorial Using a Function
def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    else:
        print('Factorial does not exist for negative numbers.')
        return None

num = int(input('Enter a number: '))
result = factorial(num)
if result is not None:
    print(f'Factorial of {num} is: {result}')

#Task 2: Using the Math Module for Calculations
import math
num = float(input("Enter a number: "))
if num <= 0:
    print("For square root and natural log, the number must be positive.")
else:
    print(f"Square root: {math.sqrt(num)}")
    print(f"Logarithm: {math.log(num)}")
print(f"Sine: {math.sin(num)}")

