"""
Program: Coffee machine (with functional programming)
Author: Subhashish Dhar
Date: 02/09/2021
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
MONEY = 0


def get_user_choice():
    """prompts the user for their choice and returns the option chosen by the user"""
    user_choice = input("What would you like? (espresso/latte/cappuccino)"
                        " or information(rates/report): ").lower()
    return user_choice


def print_report():
    """prints the amount of water, milk, coffee and money in the machine"""
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${MONEY}")


def print_rates():
    """prints the menu card of available beverages and their cost"""
    print(f"Espresso : ${MENU['espresso']['cost']}")
    print(f"Latte : ${MENU['latte']['cost']}")
    print(f"Cappuccino : ${MENU['cappuccino']['cost']}")


def check_resources_sufficient(beverage):
    """takes in a beverage and returns a warning message if any resource is not sufficient for it"""
    if resources['water'] < MENU[beverage]['ingredients']['water']:
        return "Sorry there is not enough water."
    if resources['coffee'] < MENU[beverage]['ingredients']['coffee']:
        return "Sorry there is not enough coffee."
    if beverage != 'espresso':
        if resources['milk'] < MENU[beverage]['ingredients']['milk']:
            return "Sorry there is not enough milk."
    return 0


def process_coins():
    """prompts the user to insert coins and returns the total value of coins inserted"""
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    return (quarter * 0.25) + (dime * 0.1) + (nickle * 0.05) + (penny * 0.01)


def validate_transaction(beverage, money_supplied):
    """
    input : the beverage selected and the money inserted
    if money sufficient, add money to machine
    returns : True is money is sufficient and False if not
    """
    global MONEY
    if money_supplied > MENU[beverage]['cost']:
        print(f"Here is ${round(money_supplied - MENU[beverage]['cost'], 2)} in change.")
        MONEY += MENU[beverage]['cost']
        return True
    if money_supplied < MENU[beverage]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        MONEY += MENU[beverage]['cost']
        return True


def make_coffee(beverage, material):
    """
    input : beverage and material
    returns : None
    """
    material['water'] -= MENU[beverage]['ingredients']['water']
    material['coffee'] -= MENU[beverage]['ingredients']['coffee']
    if beverage != 'espresso':
        material['milk'] -= MENU[beverage]['ingredients']['milk']
    print(f"Here is your {beverage} ☕. Enjoy!")


while True:
    chosen_option = get_user_choice().lower()

    if chosen_option == 'rates':
        print_rates()
        continue
    elif chosen_option == 'report':
        print_report()
        continue
    elif chosen_option in ('espresso', 'latte', 'cappuccino'):
        resource_shortage = check_resources_sufficient(chosen_option)
        if resource_shortage:
            print(resource_shortage)
            continue
    elif chosen_option == 'off':
        print("Machine powering off!")
        break
    else:
        print("Please select one of the given options only.")
        continue

    money_inserted = process_coins()
    if validate_transaction(chosen_option, money_inserted):
        make_coffee(chosen_option, resources)
