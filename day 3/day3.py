# odd and even
number = int(input("Enter your Number to find odd or even "))
if number%2==0:
    print("even")
else:
    print("odd")

# leap yaer logoc
year = int(input("Enter your year to find leap yaer "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
