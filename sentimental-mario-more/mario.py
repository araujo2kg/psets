import cs50

while True:
    n = cs50.get_int("Height: ")
    if n in range(1, 9):
        break

blank = n
for i in range(1, n+1):
    blank -= 1
    print(" " * blank, end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)
