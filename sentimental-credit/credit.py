import sys
from cs50 import get_int


def main():
    # Get card as int
    card = get_int("Number: ")

    # Checks card length
    length = len(str(card))
    if not 13 <= length <= 16:
        print("INVALID")
        sys.exit()

    # Check card type
    type = check_type(card, length)
    if type == "INVALID":
        print("INVALID")
        sys.exit()

    # Check card digits sum
    sum = check_sum(card, length) % 10

    # If sum is correct (0) the card is valid
    if sum == 0:
        print(type)
        sys.exit()
    else:
        print("INVALID")
        sys.exit()


def check_type(card, length):
    card = str(card)
    first_digit = card[0]
    first_two = card[:2]

    if ((length == 15) and (first_two == "37" or first_two == "34")):
        return "AMEX"
    elif ((length == 13 or length == 16) and (first_digit == "4")):
        return "VISA"
    elif ((length == 16) and (first_two in ["51", "52", "53", "54", "55"])):
        return "MASTERCARD"
    else:
        return "INVALID"


def check_sum(card, length):
    card = str(card)
    sum = 0
    digit = 0
    # Iterate from the end of the card (length-1), to the beginning (-1 End not inclusive)
    for i in range(length-1, -1, -1):
        # Get digit
        digit = int(card[i])
        # Add digit to the total sum
        if ((length - 1 - i) % 2) == 0:
            sum += digit
        else:
            if ((digit * 2) > 9):
                sum += ((digit * 2) - 9)
            else:
                sum += (digit * 2)
    return sum


if __name__ == "__main__":
    main()
