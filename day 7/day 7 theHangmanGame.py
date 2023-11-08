import random
from stages import *
from word import *

print(logo)
chosen_word = random.choice(WordBank)
black_space = ['_' for x in range(len(chosen_word))]
life = len(stages)-1
# print(chosen_word)
print(f'you have total {life} life ')
gameOver = False
while not gameOver:
    print(black_space)
    userInput = input('Enter your letter ').lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == userInput:
            black_space[position] = chosen_word[position]
    if userInput not in chosen_word:
        life -= 1
        print(stages[life])
        print(f'you left with {life} life')
        if life == 0:
            gameOver = True
            print(black_space)
            print('you loss')


    if '_' not in black_space:
        gameOver = True
        print(black_space)
        print('you won')





