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

profit = 0
MENU['espresso']['ingredients']["milk"] = 0


def resources_res(report_info):
    """
    We want to get the current resources info and print it out.
    :param report_info: string
    :return: str
    """
    if report_info == 'report':
        water_amount = resources['water']
        milk_amount = resources['milk']
        coffee_amount = resources['coffee']
        return f'Water: {water_amount}ml\nMilk: {milk_amount}ml\nCoffee: {coffee_amount}g\nMoney: ${profit:.2f}'


def check_resources(coffee_name1):
    """
    we want to check whether we have enough ingredients for making a new coffee
    Once we find one short storage of ingredients, the info will be printed out.
    :param coffee_name1: string
    :return: bool
    """
    for item in MENU[coffee_name1]['ingredients']:
        if MENU[coffee_name1]['ingredients'][item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def coffee_price_num(coffee_name2):
    """
    We want to get the price of selected coffee.
    :param coffee_name2: string
    :return: float
    """
    return MENU[coffee_name2]['cost']


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


def check_transaction(coffee1, pay_money, coffee_money):
    """
    Check whether payment is enough for purchasing a coffee.
    :param coffee1: str
    :param pay_money: integer
    :param coffee_money: int
    :return: bool
    """
    global profit
    if pay_money >= coffee_money:
        changes = round(pay_money - coffee_money, 2)
        profit += coffee_money
        resources['water'] = resources['water'] - MENU[coffee1]['ingredients']["water"]
        resources['milk'] = resources['milk'] - MENU[coffee1]['ingredients']["milk"]
        resources['coffee'] = resources['coffee'] - MENU[coffee1]['ingredients']["coffee"]
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
    elif coffee not in ['report', 'off', 'espresso', 'latte', 'cappuccino']:
        print('Not valid order!')
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
