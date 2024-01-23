import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        break
    except ValueError:
        continue

random_int = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        elif guess < random_int:
            print("Too small!")
            continue
        elif guess > random_int:
            print("Too large!")
            continue
        elif guess == random_int:
            print("Just right!")
            exit()
    except ValueError:
        continue

