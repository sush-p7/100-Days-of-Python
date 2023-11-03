import art
# print(art.logo)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operation = {'+': add, '-': sub, '*': mul, '/': div}
def calculator():
    isMoreCalculation = False
    print(art.logo)
    num1 = float(input("Enter first number: "))
    while not isMoreCalculation:

        for symbol in operation:
            print(symbol)
        operation_symbol = input('Enter your operation symbol to perform a opration ')
        function = operation[operation_symbol]
        num2 = float(input("Enter second number: "))
        answer = function(num1, num2)
        print(f"The answer of {num1} {operation_symbol} {num2} is: {answer}")
        choise = input("Do you want to perform more calculations? (y/n) ")
        if choise == 'y':
            num1 = answer
        else:
            isMoreCalculation = True
            calculator()

calculator()