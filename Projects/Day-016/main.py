from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def calculate_money():
    quarters = int(input("Enter number of quarters : "))
    dimes = int(input("Enter number of dimes : "))
    nickels = int(input("Enter number of nickels : "))
    pennies = int(input("Enter number of pennies : "))
    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)
while True:
    user_input = (input(f"What would you like to have? {menu.get_items()} :\n")).lower()
    if user_input == "off":
        break
    elif user_input == "report":
        coffeemaker.report()
    else:
        if coffeemaker.is_resource_sufficient(menu.find_drink(user_input)):
            if moneymachine.make_payment(menu.find_drink(user_input).cost):
                coffeemaker.make_coffee(menu.find_drink(user_input))
                print(f"Profit : {moneymachine.report()}")
