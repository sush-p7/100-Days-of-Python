import random
# Rock
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
Q = True
while Q:
    InputChoise = int(input('Enter 1 for Rock, 2 for Paper and 3 for Scissors and 4 for exit '))

    if InputChoise == 4:
        break

    if InputChoise == 1:
        print(Rock)
    elif InputChoise == 2:
        print(Paper)
    elif InputChoise == 3:
        print(Scissors)


    randomChoise = random.randint(1,3)
    if (InputChoise==1 and randomChoise==2):
        print(Paper)
        print("You lost !!")
    elif (InputChoise==2 and randomChoise==3):
        print(Scissors)
        print("You lost !!")
    elif (InputChoise==3 and randomChoise==1):
        print(Rock)
        print("You lost !!")

    elif (InputChoise==2 and randomChoise==1):
        print(Rock)
        print("You Win !!")
    elif (InputChoise==3 and randomChoise==2):
        print(Paper)
        print("You Win !!")
    elif (InputChoise==1 and randomChoise==3):
        print(Scissors)
        print("You Win !!")
    else:
        if InputChoise == 1:
            print(Rock)
        elif InputChoise == 2:
            print(Paper)
        elif InputChoise == 3:
            print(Scissors)
        print("Game tai")



    print("End ============================================================================")
    print("Next round ")