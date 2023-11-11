from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_off = False
coffeeMachine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
coffeeMachine.report()
money_machine.report()
while not is_off:
    choice = input(f"What would you like? ({menu.get_items()}) ")
    if choice == 'off':
        is_off = True
    elif 'report' == choice:
        coffeeMachine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMachine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeeMachine.make_coffee(drink)





