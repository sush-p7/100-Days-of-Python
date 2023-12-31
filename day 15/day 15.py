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


def is_resource_sufficient(order_ingredient):
    """return True is ingredients are sufficient else Fale"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


def process_coins():
    """return total coin value"""

    total = int(input('insert your quarters : ')) * 0.25
    total += int(input('insert your dimes : '))*0.10
    total += int(input('insert your nickles : '))*0.05
    total += int(input('insert your pennies : '))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return True is money is sufficient else False"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is your {drink_name} ☕ ")


profit = 0
isOn = True
while isOn:
    choice = input("What would you like? (espresso/latte/cappuccino) ")
    if choice == 'off':
        isOn = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}m1')
        print(f'Milk: {resources["milk"]}m1')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
