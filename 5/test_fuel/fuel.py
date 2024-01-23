def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    try:
        fraction = fraction.split("/")
        x = int(fraction[0])
        y = int(fraction[1])
        if x <= y:
            fuel = round((x / y) * 100)
            return fuel
        if y == 0:
            raise ZeroDivisionError("Invalid divisor(0)")
    except ValueError:
        raise ValueError("Invalid input format (X/Y)")


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
