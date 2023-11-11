from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
choice = input(f"What would you like? ({Menu().get_items()}) ")
if 'report'== choice:
    coffeeMachine.report()
else:





