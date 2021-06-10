from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money = MoneyMachine()

while True:
    user_option = input(f"What would you like? ({my_menu.get_items()}) or report?: ").lower()
    if user_option == 'off':
        print("Machine powering off...")
        break
    elif user_option == 'report':
        my_coffee_maker.report()
        my_money.report()
    # elif not my_menu.find_drink(user_option):
    #     print(f"We don't have {user_option}. Please order something from the menu!")
    # elif my_coffee_maker.is_resource_sufficient(my_menu.find_drink(user_option)):
    #     chosen_beverage = my_menu.find_drink(user_option)
    #     if my_money.make_payment(chosen_beverage.cost):
    #         my_coffee_maker.make_coffee(chosen_beverage)
    else:
        chosen_beverage = my_menu.find_drink(user_option)
        if my_coffee_maker.is_resource_sufficient(chosen_beverage) and my_money.make_payment(chosen_beverage.cost):
            my_coffee_maker.make_coffee(chosen_beverage)
