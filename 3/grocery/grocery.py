grocery = []
cart = []

while True:
    try:
        item = input().upper()
        grocery.append(item)
        for item in grocery:
            if item not in cart:
                cart.append(item)
                cart.sort()
    except EOFError:
        for item in cart:
            print(grocery.count(item), item)
        break
