import random
WordBank = ['butterfly', 'mouse', 'sunflower', 'ocean', 'rainbow', 'book',
            'guitar', 'coffee', 'mountain', 'apple',
            'bicycle', 'firefly', 'camera', 'chocolate', 'keyboard',
            'piano', 'laughter', 'adventure', 'moonlight', 'whisper',
            'cloud', 'sandcastle', 'treasure', 'journey', 'carousel',
            'wonderland',
            'candlelight', 'strawberry', 'waterfall', 'telescope']

chosen_word = random.choice(WordBank)
black_space = ['_' for x in range(len(chosen_word))]

userInput = input('Enter your letter ').lower()
index = 0
for letter in chosen_word:
    if letter == userInput:
        print('yes')
        black_space[index]=letter
        index +=1
    else:
        print('no')
        index += 1

print(black_space)
print(chosen_word)