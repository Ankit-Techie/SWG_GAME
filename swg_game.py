import random
import time
g = "Snake", "Gun", "Water"
n = 1
comp = 0
user = 0
while n <= 10:
    a = random.choice(g)
    print("Enter your Choice s for snake, g for gun and w for water:")
    b = input()
    time.sleep(1)
    if a == "Snake":
        print("Snake")
        if b == "s" or b == "S":
            print("It's a  tie")
        elif b == "g" or b == "g":
            user += 1
            print("It was your Chance")
        elif b == "w" or b == "W":
            comp += 1
            print("It was computer chance")
        else:
            print("error")
    elif a == "Gun":
        print("Gun")
        if b == "s" or b == "S":
            comp += 1
            print("It was computer chance ")
        elif b == "g" or b == "G":
            print("It was a tie")
        elif b == "w" or b == "W":
            user += 1
            print("It was your chance")
        else:
            print("error")
    elif a == "Water":
        print("Water")
        if b == "s" or b == "S":
            user += 1
            print("It was your chance")
        elif b == "g" or b == "G":
            comp += 1
            print("It was computer chance")
        elif b == "w" or b == "W":
            print("It was a tie")
        else:
            print("error")
    n += 1
    print("Your score", user)
    print("Computer Score", comp)

if user > comp:
    print("You Won")
elif comp > user:
    print("Comp won")
else:
    print("It's a tie")
