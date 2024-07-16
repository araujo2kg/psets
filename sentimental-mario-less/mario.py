import cs50

height = 0
while True:
    height = cs50.get_int("Height: ")
    if 1 <= height <= 8:
        break

blank = height
for brick in range(1, height+1):
    blank -= 1
    print(" " * blank, end="")
    print("#" * brick)
