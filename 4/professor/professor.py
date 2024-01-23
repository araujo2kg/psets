import random


def main():
    level = get_level()
    counter = 0
    score = 0
    eee = 0
    answer = -1

    while counter < 10:
        x, y, result = generate_integer(level)
        counter += 1
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            pass
        if answer == result:
            score += 1
            continue
        elif answer != result:
            eee += 1
            print("EEE")
            for b in range(2):
                try:
                    answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    pass
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
                    eee += 1
                    if eee == 3:
                        print(f"{x} + {y} = {result}")
                        eee = 0
                        break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    result = x + y
    return x, y, result


if __name__ == "__main__":
    main()
