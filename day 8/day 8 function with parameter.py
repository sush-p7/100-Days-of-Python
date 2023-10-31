def greet(name , location):
    print(f"hello {name}")
    print(f"what is it like in {location}")

print('Positional Arguments\n')
greet('Sushant','India\n')
greet('India','Sushant\n\n\n')
print('Keyword Arguments\n')
greet(location='India',name='Sushant\n')
greet(name='Sushant',location='India')

'''
Positional Arguments: Arguments passed in correct positional order (the method name implied by the order). In the third line greet('Sushant','India'), 'Sushant' is passed as name and 'India' as location by their position.
Keyword Arguments: When you use keyword arguments in a function call, the caller identifies the arguments by parameter name. In Python, you can also mix positional arguments with keyword arguments during a function call.greet(name='Sushant',location='India')'''