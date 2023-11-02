from replit import clear
from art import logo

print(logo)

biders = {}
isBidEnd = False
while not isBidEnd:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    biders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        isBidEnd = True
    else:
        clear()
        print(logo)
winner = max(biders, key=biders.get)
print(f"The winner is {winner} with a bid of ${biders[winner]}")

