#swapping numbers :
a = int(input("enter first number "))
b = int(input("enter second number "))
#swapping logic

c = a
a = b
b = c
print(f'a is {a} and b is {b}')

#without using 3rd variable
a , b = b , a
print(f'a is {a} and b is {b}')


