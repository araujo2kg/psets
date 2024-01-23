menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0

while True:
    try:
        request = input("Item: ").title().strip()
        if request in menu:
            order = menu[request]
            total = total + order #can reduce to total += menu[request]
            print(f"Total: ${total:.2f}") # .2f = limit to 2 decimal points
            continue
        else:
            continue
    except ValueError:
        pass
    except NameError:
        pass
    except EOFError:
        print()
        break
    except KeyError:
        continue
    else:
        break

