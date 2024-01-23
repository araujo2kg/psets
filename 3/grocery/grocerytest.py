grocery = {}

while True:
    try:
        item = input().upper()

    except EOFError:
        for item in sorted(grocery):
            print(grocery[item], item)
        break
    if item in grocery:
        grocery[item] += 1

    else:
        grocery[item] = 1
