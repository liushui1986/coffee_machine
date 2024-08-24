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

resources['money'] = 0
MENU['espresso']['ingredients']["milk"] = 0


def resources_res(report_info):
    if report_info == 'report':
        water_amount = resources['water']
        milk_amount = resources['milk']
        coffee_amount = resources['coffee']
        profit_amount = resources['money']
        return f'Water: {water_amount}ml\nMilk: {milk_amount}ml\nCoffee: {coffee_amount}g\nMoney: ${profit_amount:.2f}'


def check_resources(coffee_name1):
    if MENU[coffee_name1]['ingredients']["water"] > resources['water']:
        print('Sorry there is not enough water.')
        return False
    elif MENU[coffee_name1]['ingredients']["milk"] > resources['milk']:
        print('Sorry there is not enough milk.')
        return False
    elif MENU[coffee_name1]['ingredients']["coffee"] > resources['coffee']:
        print('Sorry there is not enough coffee.')
        return False
    else:
        return True


def coffee_price_num(coffee_name2):
    if coffee_name2 == "espresso":
        return MENU['espresso']['cost']
    elif coffee_name2 == "latte":
        return MENU['latte']['cost']
    elif coffee_name2 == "cappuccino":
        return MENU['cappuccino']['cost']
    else:
        return 0


def total_pay(quarter, dime, nickle, penny):
    """
    Calculate the total payment
    :param quarter: integer
    :param dime: int
    :param nickle: int
    :param penny: int
    :return: float
    """
    return 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny


def check_transaction(coffee_name3, pay_money, coffee_money):
    """
    Check whether payment is enough
    :param pay_money: integer
    :param coffee_money: int
    :return: bool
    """
    if pay_money >= coffee_money:
        changes = float(pay_money - coffee_money)
        resources['money'] += coffee_money
        resources['water'] = resources['water'] - MENU[coffee_name3]['ingredients']["water"]
        resources['milk'] = resources['milk'] - MENU[coffee_name3]['ingredients']["milk"]
        resources['coffee'] = resources['coffee'] - MENU[coffee_name3]['ingredients']["coffee"]
        print(f'Here is ${changes:.2f} in change.')
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False


while True:
    coffee = input('What would you like? (espresso/latte/cappuccino): \n').lower()
    if coffee == 'report':
        result = resources_res('report')
        print(result)
    elif coffee == 'off':
        break
    elif check_resources(coffee):
        print('Please insert coins.')
        quarters = int(input('How many quarters?: '))
        dimes = int(input('How many dimes?: '))
        nickles = int(input('How many nickles?: '))
        pennies = int(input('How many pennies?: '))
        pay_amount = total_pay(quarters, dimes, nickles, pennies)
        coffee_price = coffee_price_num(coffee)
        if check_transaction(coffee, pay_amount, coffee_price):
            print(f'Here is your {coffee}. Enjoy!')
