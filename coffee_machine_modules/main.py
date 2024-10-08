from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


item = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    options = item.get_items()
    choice = input(f'What would you like? ({options}): ')
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        break
    else:
        drink = item.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
