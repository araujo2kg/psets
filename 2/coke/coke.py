coke = 50

while True:
    coin = int(input("Insert a coin (5, 10, 25): "))

    if coin == 5 and coke > 4:
        coke = coke - coin
        if coke == 0:
                print("Change Owed: 0")
                break
        else:
             print(f"Amount Due: {coke}")

    elif coin == 10 and coke > 9:
        coke = coke - coin
        if coke == 0:
                print("Change Owed: 0")
                break
        else:
             print(f"Amount Due: {coke}")

    elif coin == 25 and coke > 24:
        coke = coke - coin
        if coke == 0:
                print("Change Owed: 0")
                break
        else:
             print(f"Amount Due: {coke}")

    elif coke < coin and coin == 5 or coin == 10 or coin == 25:
         coke = coke - coin
         coke = coke * -1 #can use abs() too
         print(f"Change Owed: {coke}")
         break

    elif coin != 5 and coin != 10 and coin != 25:
        print(f"Invalid coin!\nAmount Due: {coke}")

