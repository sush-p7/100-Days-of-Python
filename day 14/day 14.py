import art
import random
import data
Data = data.data

print(art.logo)
gameOver = False
print(random.choice(Data))
score = 0
while not gameOver:
    A = random.choice(Data)
    B = random.choice(Data)
    print(f'Compare A: {A["name"]}, a {A["description"]} from {A["country"]}')
    print(art.vs)
    print(f'Against B: {B["name"]}, a {B["description"]} from {B["country"]}')
    answer = input("Who has more follower? type 'A' or 'B':")
    if (answer == 'A' and int(A['follower_count']) > int(B['follower_count'])) or (answer == 'B' and int(B['follower_count'])>int(A['follower_count'])):
        score+=1
        print(f'Yor are right! Current score is {score}')
    else:
        print(f'Sorry, that was wrong . your final score is {score}')
        gameOver = True

