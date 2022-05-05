"""
Program: Calculator
Author: Subhashish Dhar
Date: 02/09/2021
"""

from calculator_art import LOGO


def add(num_1, num_2):
    """Add n1 and n2 and return sum"""
    return num_1 + num_2


def subtract(num_1, num_2):
    "Subtract n2 from n1 and return difference"
    return num_1 - num_2


def multiply(num_1, num_2):
    """multiply n1 and n2 and return product"""
    return num_1 * num_2


def divide(num_1, num_2):
    """divide n1 by n2 and return result"""
    return num_1 / num_2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

print(LOGO)
num1 = float(input("What's the first number?: "))
for operation in operations:
    print(operation)

TO_CONTINUE = True

while TO_CONTINUE:
    operation = input("Pick an operation: ")
    while operation not in operations:
        operation = input("Pick a proper operation: ")
    num2 = float(input("What's the next number?: "))
    calculation = operations[operation]
    answer = calculation(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    choice = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: "
    )
    if choice == "n":
        TO_CONTINUE = False
    num1 = answer
