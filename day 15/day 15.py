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
    "coffee": 0,
    'money': 0,
}
money = 0

def collect_money(product):
    MENU_product = MENU[product]
    quarters = int(input('insert your quarters : '))
    dimes = int(input('insert your dimes : '))
    nickles = int(input('insert your nickles : '))
    pennies = int(input('insert your pennies : '))
    if float(MENU_product['cost']) <= float((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)):
        return_money = float((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)) - float(MENU_product['cost'])

        resources['money'] +=  float((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01))
        return return_money
    else:
        print("you Dont have enough money ")
        return False

def check_resources(product):
    MENU_product = MENU[product]
    if product == "espresso":
        need_water = MENU_product['ingredients']['water']
        need_coffee = MENU_product['ingredients']['coffee']
        need_milk = 0
    else:
        need_water = MENU_product['ingredients']['water']
        need_coffee = MENU_product['ingredients']['coffee']
        need_milk = MENU_product['ingredients']['milk']
    if int(resources['water'])>= int(need_milk) and int(resources['water'])>= int(need_water) and int(resources['coffee'])>= int(need_coffee):
        money_return = collect_money(product)
        if money_return:
            resources['water'] = resources['water']-need_water
            resources['milk'] = resources['milk'] -need_milk
            resources['coffee'] = resources['coffee'] -need_coffee
            return money_return

        else:
            return False


# money = 0
def user_choise():
    user_input = input("What would you like? (espresso/latte/cappuccino) ")
    if user_input in ['off','Off','OFF']:
        print("Machine is turn off for maintenance  ")
        return True
    return user_input
machine = False
while not machine:
    user_input = user_choise()
    if user_input == True:
        machine = True
    elif user_input == "report":
        # resources['money'] = money
        print(resources)
    elif "espresso" == user_input:
        return_resource=check_resources(user_input)
        if return_resource!=True:
            print(f"Enjoy your coffee and here is your chnage {return_resource}")
        else:
            break




