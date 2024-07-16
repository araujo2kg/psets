import cs50

while True:
    n = cs50.get_int("Height: ")
    if n in range(1, 9):
        break

for brick in range(1, n+1):
    for blank in range(n - brick):
        print(" ", end="")
    print("#" * brick)
