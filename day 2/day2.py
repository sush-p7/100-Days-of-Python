# Import the necessary modules
weigth = int(input("enter your weigth in killogram "))  # Request the user's weight in kilograms
heigth = float(input("enter you heigth in meter "))  # Request the user's height in meters

bmi = weigth/heigth*heigth # Calculate the user's BMI using the formula weight / (height ^ 2)

print(f'your BMI is {int(bmi)}')  # Print the user's BMI