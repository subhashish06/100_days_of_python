from calculator_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
                 '+': add,
                 '-': subtract,
                 '*': multiply,
                 '/': divide
             }

print(logo)
num1 = float(input("What's the first number?: "))
for operation in operations:
    print(operation)

to_continue = True

while to_continue:
    operation = input("Pick an operation: ")
    while operation not in operations:
        operation = input("Pick a proper operation: ")
    num2 = float(input("What's the next number?: "))
    calculation = operations[operation]
    answer = calculation(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if choice == 'n':
        to_continue = False
    num1 = answer
