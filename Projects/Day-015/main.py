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


def print_report():
    print(f"Water : {resources['water']} ")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")


def is_resource_sufficient(coffee_type):
    if MENU[coffee_type]['ingredients']['water'] <= resources['water']:
        if MENU[coffee_type]['ingredients']['coffee'] <= resources["coffee"]:
            if coffee_type == 'espresso':
                return "true"
            elif MENU[coffee_type]['ingredients']['milk'] <= resources['milk']:
                return "true"
            else:
                return "milk"
        else:
            return "coffee"
    else:
        return "water"


def calculate_monetary(quarters, dimes, nickles, pennies):
    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies


def update_resources(user_choice):
    global resources
    resources['water'] -= MENU[user_choice]['ingredients']['water']
    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']

    if user_choice != "espresso":
        resources['milk'] -= MENU[user_choice]['ingredients']['milk']


def coffee_machine():
    while True:
        user_choice = (input("What would you like? (espresso/latte/cappuccino):")).lower()
        if user_choice == "report":
            print_report()
        elif user_choice == "off":
            break
        else:
            enough_resources = is_resource_sufficient(user_choice)
            if enough_resources == "true":
                print("Please insert coins")
                quarters = int(input("Enter number of quarters : "))
                dimes = int(input("Enter number of dimes : "))
                nickles = int(input("Enter number of nickles : "))
                pennies = int(input("Enter number of pennies : "))
                amount_received = calculate_monetary(quarters, dimes, nickles, pennies)

                if amount_received < MENU[user_choice]['cost']:
                    print(f"Sorry that's not enough money. Money refunded")
                elif amount_received == MENU[user_choice]['cost']:
                    update_resources(user_choice)
                    print(f"Here's your {user_choice}. Enjoy!!")
                else:
                    update_resources(user_choice)
                    return_amount = round(amount_received - MENU[user_choice]['cost'], 2)
                    print(f"Here is ${return_amount} in change.")
            else:
                print(f"Sorry there is not enough {resources}.")


coffee_machine()
