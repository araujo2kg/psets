while True:
    try:
        fraction = input("Fraction: ").split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        if x <= y:
            fuel = round((x / y)*100)
            if fuel >= 99:
                print("F")
            elif fuel <= 1:
                print("E")
            else:
                print(fuel, "%", sep="")
                break
        else:
            continue
    except ValueError:
        print("Invalid input format (X/Y)")
    except ZeroDivisionError:
        print ("Invalid divisor(0)")
    else:
        break

