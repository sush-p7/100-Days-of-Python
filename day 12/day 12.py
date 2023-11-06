import random
import art
def greet():
    print(art.logo)
    print("Welcome To The Number Guessing Game !\nI'm Thinking The number is Between 1 to 100")
    Chance = input('Choose a Difficulty. Type "easy" or "hard" ')
    if Chance == 'easy':
        return 10
    elif Chance == 'hard':
        return 5

def guess_number():
    return random.randint(0,100)
def game():
    Chance = greet()
    answer = int(guess_number())
    for i in range(Chance):
        print(f'You have {10-i} attempts remaining to guess the number ')
        guess = int(input("Make your Guess : "))
        if guess > answer:
            print("Too High")
        elif guess < answer:
            print("Too Low")
        elif answer == guess:
            print(f"You got it ! the correct answer was {answer}")
game()